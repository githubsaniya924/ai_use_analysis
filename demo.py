import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("ai_use_dataset_final.csv")
    return df

df = load_data()

import plotly.express as px

# Count the occurrences of each AI tool used
df_ai_tools = df["AI_Tools_Used"].value_counts().reset_index()

# Rename columns for clarity
df_ai_tools.columns = ["AI Tool", "Usage Count"]

# Create a donut chart
fig = px.pie(df_ai_tools, 
             names="AI Tool", 
             values="Usage Count", 
             title="AI Tool Usage Distribution",
             hole=0.4,  # Creates the donut effect
             color_discrete_sequence=px.colors.qualitative.Set3)  # Soft and diverse colors

# Customize layout for better visibility
fig.update_layout(
    font=dict(size=14, color="black"),  # Better font size and color
    legend_title="AI Tools",
    showlegend=True
)

fig.show()

        # df_students = df[df['User_Type'] == 'Student']
        # df_employees = df[df['User_Type'] == 'Employee']

        # # Creating scatter plots
        # fig_students = px.scatter(df_students, 
        #                         x="AI_Tools_Used", 
        #                         y="Frequency of AI Use", 
        #                         size="Perceived Increase in Productivity (%)", 
        #                         title="Most Used AI Tools by Students",
        #                         labels={"AI_Tools_Used": "AI Tool", "Frequency of AI Use": "Usage Frequency"},
        #                         color="AI_Tools_Used")

        # fig_employees = px.scatter(df_employees, 
        #                         x="AI_Tools_Used", 
        #                         y="Frequency of AI Use", 
        #                         size="Perceived Increase in Productivity (%)", 
        #                         title="Most Used AI Tools by Employees",
        #                         labels={"AI_Tools_Used": "AI Tool", "Frequency of AI Use": "Usage Frequency"},
        #                         color="AI_Tools_Used")

        # # Combining both figures side by side
        # fig = go.Figure()
        # for trace in fig_students.data:
        #     fig.add_trace(trace)

        # for trace in fig_employees.data:
        #     fig.add_trace(trace)

        # # Adjusting layout to place charts side by side
        # fig.update_layout(
        #     title="Comparison of AI Tools Used by Students vs. Employees",
        #     xaxis=dict(title="AI Tools Used"),
        #     yaxis=dict(title="Usage Frequency"),
        #     grid=dict(columns=2, rows=1),
        #     showlegend=False
        # )

        # st.plotly_chart(fig)
            

        # Count the occurrences of each AI tool used
        # df_ai_tools = df["AI_Tools_Used"].value_counts().reset_index()

        # # Rename columns for clarity
        # df_ai_tools.columns = ["AI Tool", "Usage Count"]

        # # Create a donut chart
        # fig = px.pie(df_ai_tools, 
        #             names="AI Tool", 
        #             values="Usage Count", 
        #             title="AI Tool Usage Distribution",
        #             hole=0.4,  # Creates the donut effect
        #             color_discrete_sequence=px.colors.qualitative.Set3)  # Soft and diverse colors

        # # Customize layout for better visibility
        # fig.update_layout(
        #     font=dict(size=14, color="black"),  # Better font size and color
        #     legend_title="AI Tools",
        #     showlegend=True
        # )

        # fig.show()

        #What are the major challenges faced in AI adoption?
        # 📝 Insight:
        # Shows top concerns & barriers in using AI.
        # Helps improve AI implementation strategies.
        # 📊 Suggested Chart: Bar Chart
        # X-axis: Challenges Faced
        # Y-axis: Number of People Reporting
        # 🔢 Code
        # python
        # Copy
        # Edit
        # Count the occurrences of each unique challenge

        # Sample dataset (replace with actual df)
        # df = pd.read_csv("your_dataset.csv")

        
# What are the major challenges faced in AI adoption?
# 📝 Insight:
# Shows top concerns & barriers in using AI.
# Helps improve AI implementation strategies.
# 📊 Suggested Chart: Bar Chart
# X-axis: Challenges Faced
# Y-axis: Number of People Reporting
# 🔢 Code
# python
# Copy
# Edit
# fig = px.bar(df["Challenges Faced"].value_counts().reset_index(), 
#              x="index", 
#              y="Challenges Faced",
#              color="index",
      
      
#              title="Major Challenges in AI Adoption",
#              labels={"index": "Challenges", "Challenges Faced": "Count"})

# fig.show()


# Which Age is using AI the most?
# 📝 Insight:
# Helps understand AI adoption trends by age.
# Useful for targeting AI training programs.
# 📊 Suggested Chart: Pie Chart
# Slices: Ages
# Size: Count of Users
# 🔢 Code
# python
# Copy
# Edit
# fig = px.pie(df, 
#              names="Age", 
#              title="AI Usage by Age",
#              hole=0.4)  # Donut chart
# fig.show()  


# Which Age is using AI the most?
# 📝 Insight:
# Helps understand AI adoption trends by age.
# Useful for targeting AI training programs.
# 📊 Suggested Chart: Pie Chart
# Slices: Ages
# Size: Count of Users
# 🔢 Code
# python
# Copy
# Edit
# fig = px.pie(df, 
#              names="Age", 
#              title="AI Usage by Age",
#              hole=0.4)  # Donut chart
# fig.show()  


# Which Ages benefit the most from AI in task time reduction?
# 📊 Visualization: Bubble Chart

# python
# Copy
# Edit
# import plotly.express as px

# df["Task Time Reduction (%)"] = ((df["Avg Task Time (Before AI)"] - df["Avg Task Time (After AI)"]) / df["Avg Task Time (Before AI)"]) * 100

# fig = px.scatter(df, 
#                  x="Age", 
#                  y="Task Time Reduction (%)", 
#                  size="Work Efficiency Score",
#                  color="User_Type",
#                  title="Task Time Reduction Due to AI Usage")

# fig.show()






# Does frequent AI use correlate with higher job promotions?
# 📊 Visualization: Scatter Plot with Color Scaling

# python
# Copy
# Edit
# import plotly.express as px

# fig = px.scatter(df, 
#                  x="Frequency of AI Use", 
#                  y="Job Promotions or Salary Increase", 
#                  color="Work Efficiency Score",
#                  title="AI Usage Frequency vs Job Promotions")

# fig.show()



# What are the top AI challenges faced by students and employees?
# 📊 Visualization: Horizontal Bar Chart

# python
# Copy
# Edit
# import plotly.express as px

# fig = px.bar(df, 
#              y="Challenges Faced", 
#              x="User_Type", 
#              color="User_Type",
#              orientation="h",
#              title="Top AI Challenges Faced by Students and Employees")

# fig.show()


# Which industries see the biggest productivity increase from AI?
# 📊 Visualization: Bar Chart

# python
# Copy
# Edit
# import plotly.express as px

# fig = px.bar(df, 
#              x="Industry", 
#              y="Perceived Increase in Productivity (%)", 
#              color="User_Type",
#              title="Productivity Increase Across Industries")

# fig.show()

#  How does AI satisfaction vary by education level?
# 📊 Visualization: Box Plot

# python
# Copy
# Edit
# import plotly.express as px

# fig = px.box(df, 
#              x="Education Level", 
#              y="Satisfaction with AI Integration", 
#              color="User_Type",
#              title="AI Satisfaction Levels Across Education Levels")

# fig.show()