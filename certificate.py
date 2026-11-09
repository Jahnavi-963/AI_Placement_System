import streamlit as st

def certificate_page(avg_score):

    st.header("🏆 Certificate")

    if avg_score >= 70:

        st.success("🎉 Congratulations!")

        st.markdown(f"""
# 🎓 Certificate of Achievement

This certificate is proudly presented to

## {st.session_state.username}

for successfully completing the

### AI Placement Interview Program

⭐ Average Score : **{avg_score:.2f}/100**

Keep Learning 🚀
""")

    else:

        st.error("Certificate Locked")

        st.info("Score at least 70 to unlock certificate.")