class RealEstateAgent:
    def __init__(self, name, total_sales, contact_info):
        self.name = name
        self.total_sales = total_sales
        self.contact_info = contact_info

class RealEstateAgency:
    def __init__(self):
        self.agents = {}

    def add_agent(self, agent):
        self.agents[agent.name] = agent

    def list_agents(self):
        for agent_name, agent in self.agents.items():
            print(f"Agent: {agent_name}")
            print(f"Total Sales: ${agent.total_sales:,}")
            print(f"Contact Info: {agent.contact_info}\n")

# Create a RealEstateAgency instance
agency = RealEstateAgency()

# Add agents
agent1 = RealEstateAgent("John Doe", 15000000, "johndoe@example.com")
agent2 = RealEstateAgent("Jane Smith", 20000000, "janesmith@example.com")

agency.add_agent(agent1)
agency.add_agent(agent2)

# List agents
print("Best Commercial Real Estate Agents in Boston:")
agency.list_agents()
