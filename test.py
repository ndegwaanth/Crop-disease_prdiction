from graphviz import Digraph

# Creating a system flowchart
flowchart = Digraph('System_Flowchart', format='png')
flowchart.attr(rankdir='TB')

# Nodes
flowchart.node('U', 'User')
flowchart.node('L', 'Login System')
flowchart.node('D', 'Data Input')
flowchart.node('C', 'Data Cleaning')
flowchart.node('P', 'Predictive Model')
flowchart.node('V', 'Visualization Dashboard')
flowchart.node('DB', 'Database')

# Edges
flowchart.edge('U', 'L', label='Enters Credentials')
flowchart.edge('L', 'D', label='Authenticated? Yes')
flowchart.edge('D', 'C', label='Submit Data')
flowchart.edge('C', 'P', label='Cleaned Data')
flowchart.edge('P', 'V', label='Predictions')
flowchart.edge('D', 'DB', label='Store Raw Data')
flowchart.edge('C', 'DB', label='Store Clean Data')
flowchart.edge('V', 'U', label='Displays Insights')

# Render and save the flowchart
flowchart_path = "/mnt/data/system_flowchart"
flowchart.render(flowchart_path)

flowchart_path + ".png"

