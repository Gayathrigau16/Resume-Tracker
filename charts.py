import matplotlib.pyplot as plt  # type: ignore

def plot_skills(found_skills , missing_skills):
    labels = ["Found Skills","Missing Skills"]
    values = [len(found_skills),len(missing_skills)]
    
    fig, ax = plt.subplots(figsize=(5,5))
    ax.pie(values , labels = labels, autopct ="%1.1f%%",startangle = 90 )
    ax.set_title("Skills Analysis")
    return fig