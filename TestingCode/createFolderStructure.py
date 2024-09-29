import os

def create_folder_and_readme(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")
    
    readme_path = os.path.join(path, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write(f"# {os.path.basename(path)}\n\nThis folder contains information about {os.path.basename(path)} in the context of Machine Learning mathematics.")
        print(f"Created README.md in: {path}")
    else:
        print(f"README.md already exists in: {path}")

def create_ml_math_folder_structure():
    structure = {
        "Linear Algebra": [
            "Vectors", "Matrices", "Eigenvalues and Eigenvectors", 
            "Matrix Decomposition", "Vector Spaces", "Linear Transformations"
        ],
        "Calculus": [
            "Derivatives", "Gradients", "Partial Derivatives", 
            "Chain Rule", "Integrals", "Taylor Series"
        ],
        "Probability and Statistics": {
            "Probability Basics": ["Random Variables", "Probability Distributions"],
            "Statistical Inference": ["Hypothesis Testing", "Confidence Intervals"],
            "Bayesian Statistics": ["Bayes' Theorem", "Bayesian Inference"]
        },
        "Optimization": [
            "Gradient Descent", "Stochastic Gradient Descent",
            "Convex Optimization", "Lagrange Multipliers",
            "Constrained Optimization"
        ],
        "Information Theory": [
            "Entropy", "Cross-Entropy", "Kullback-Leibler Divergence",
            "Mutual Information"
        ]
    }

    for category, items in structure.items():
        create_folder_and_readme(category)
        
        if isinstance(items, list):
            for item in items:
                create_folder_and_readme(os.path.join(category, item))
        elif isinstance(items, dict):
            for subcategory, subitems in items.items():
                subcategory_path = os.path.join(category, subcategory)
                create_folder_and_readme(subcategory_path)
                for subitem in subitems:
                    create_folder_and_readme(os.path.join(subcategory_path, subitem))

    print("Machine Learning Math folder structure creation and README.md file addition completed!")

if __name__ == "__main__":
    create_ml_math_folder_structure()