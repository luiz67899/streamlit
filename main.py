import streamlit as st
from streamlit_option_menu import option_menu
import about, account, home, trending, your_posts

st.set_page_config(
  page_title="Pondering"
)

class MultiApp:

    def __init__(self):
        # Create list of apps
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        # Create a side bar 
        with st.sidebar:
            app = option_menu(
                # Title
                menu_title='Pondering',
                options=['Home', 'Account', 'Trending', 'Your Posts', 'About'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle'],
                # Title icon
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == 'Home':
            home.app()
        elif app == 'Account':
            account.app()
        elif app == 'Trending':
            trending.app()
        elif app == 'Your Posts':
            your_posts.app()
        elif app == 'About':
            about.app()

app = MultiApp()
app.run()
