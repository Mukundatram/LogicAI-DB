import streamlit as st # type: ignore
import requests
import pandas as pd # type: ignore

API_URL = "http://localhost:8000/query"

st.set_page_config(page_title="Agentic SQL Assistant", layout="centered")

st.title("🧠 Agentic SQL Assistant")
st.caption("Ask questions. Agent plans. Database answers.")

# Input box
question = st.text_area(
    "Ask a question about your data",
    placeholder="e.g. Show top 10 most populated cities",
    height=100
)

if st.button("Run Query"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=120
                )

                if response.status_code != 200:
                    st.error(f"API Error: {response.status_code}")
                else:
                    data = response.json()

                    # ---- PLAN / SQL ----
                    st.subheader("🧩 Agent Plan / SQL")
                    st.code(data.get("plan", "No plan returned"), language="sql")

                    # ---- ERROR ----
                    if data.get("error"):
                        st.subheader("❌ Error")
                        st.error(data["error"])
                        st.stop()

                    # ---- ROWS ----

                    rows = data.get("rows")

                    if rows:
                        st.subheader("📊 Query Results")

                        try:
                            # If backend sends rows only (list of lists)
                            if isinstance(rows, list) and len(rows) > 0 and isinstance(rows[0], list):
                                # Try to infer column names from SQL
                                sql = data.get("plan", "")
                                columns = []

                                if "select" in sql.lower():
                                    try:
                                        select_part = sql.lower().split("from")[0]
                                        columns = [
                                            col.strip().split()[-1]
                                            for col in select_part.replace("select", "").split(",")
                                        ]
                                    except Exception:
                                        columns = [f"col_{i}" for i in range(len(rows[0]))]
                                else:
                                    columns = [f"col_{i}" for i in range(len(rows[0]))]

                                df = pd.DataFrame(rows, columns=columns)
                            elif isinstance(rows, list) or isinstance(rows, dict):
                                df = pd.DataFrame(rows)
                            else:
                                st.error("Returned data is not in a valid table format.")
                                st.stop()

                            st.dataframe(
                                df,
                                use_container_width=True,
                                hide_index=True
                            )

                            st.caption(f"Returned {len(df)} rows")
                        except Exception as e:
                            st.error(f"Failed to display results: {e}")
                            st.stop()
                    else:
                        st.info("No rows returned.")

                    # ---- SUMMARY ----
                    if data.get("summary"):
                        st.subheader("📝 Summary")
                        st.write(data["summary"])

            except requests.exceptions.RequestException as e:
                st.error(f"Failed to reach API: {e}")
