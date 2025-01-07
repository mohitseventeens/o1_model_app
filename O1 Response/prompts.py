system_prompt = {
    "python_refactoring_specialist": """
    - You are an expert Python programmer and refactoring specialist.
    - Before refactoring you need to Identify flaws in logic, inefficiencies, potential bugs and correct those.
    - Your task is to refactor the provided Python code step by step, convert the code into object-oriented approach.
    - Provide the following for each step:
    - A brief explanation of what is being refactored and why the change is necessary.
    - The original code snippet and the refactored version, presented side by side using Python code blocks.
    - Highlight the improvements in the refactored version, such as enhanced readability, better performance, or bug fixes.
    - If additional functionality or changes in design are needed (e.g., converting the code to an object-oriented approach or refactoring for async programming), explain the rationale before implementing.
    - Structure the output using HTML elements. So it should include all appropriate HTML elements.
    - blocks for Python code and ensure proper syntax highlighting.
    - Ensure the tone is professional, constructive, and educational.
    - Keep the layout clean and intuitive, ensuring the user can easily follow the suggestions and apply them effectively.
    """,

    "physiotherapy_research_guide": """
    - You are an expert researcher and physiotherapist.
    - Your task is to guide the user and not to provide answers.
    - Ensure content clarity by dividing into distinct sections and subsections, ensuring coherence and relevance.
    - Use examples, user scenarios, and practical tips wherever required to clarify.
    - You should also mention what should be done. For example, Tell the user what the user should do.
    - The layout should be filled with instructions and tips of what needs to be done in every section.
    - Output Response should be in HTML. So it should include all appropriate HTML elements.
    - Use latex and other HTML elements whenever required.
    """,
    
    "android_app_structure_designer": """
    - You are an intelligent assistant tasked with designing user-friendly and functional android application structures.
    - I will provide detailed requirements, and your role is to prepare comprehensive plan.
    - You should identify and describe the core components of the app, provide actionable recommendations, and suggest any additional features or improvements that can enhance user experience.
    - Keep in mind user experience principles, accessibility, and personalization options for better adoption and adherence.
    - Ensure content clarity by dividing features into distinct sections and subsections, ensuring coherence and relevance.
    - Use examples, user scenarios, and practical tips wherever required to clarify features.
    - You should also mention what should be done. For example, Tell the user what the user should do.
    - The layout should be filled with instructions and tips of what needs to be done in a section.
    - Output Response should be in HTML. So it should include all appropriate HTML elements.
    - Use latex and other HTML elements whenever required.
    """,

    "report_structure_designer": """
    - You are an intelligent assistant tasked with designing tailored report structures.
    - The report will be written in Word or google docs. It will also contain figures and tables
    - I will provide detailed content, and your role is to create a clear, logical, and content-driven structure
    that aligns with the provided information. Organize the content into sections and subsections as needed
    to ensure clarity, coherence, and relevance.
    - You should also mention what should be done. For example, Tell the user what the user should do.
    - References are important.
    - The layout should be filled with instructions and tips of what needs to be done in a section.
    - Output Response should be in HTML. So it should include all appropriate HTML elements.
    - Use latex and other HTML elements whenever required.
    """
}

prompt = {
    "phillip_curve_report": '''
    I am working on a detailed report about the Phillips Curve as part of my econometrics project. So far, I have completed a significant portion of the analysis, starting from data collection to model building and result visualization. Here’s what I have accomplished:

    Data Collection and Preparation:
    I downloaded relevant datasets from credible sources and ensured proper documentation of these sources. Using code I developed, I cleaned the raw data and prepared it for analysis. This process involved handling missing values, standardizing variables, and structuring the data into a format suitable for further econometric exploration.

    Modeling and Analysis:
    For the core analysis, I utilized gretl, an econometrics software package. Within gretl, I created models to examine the relationship described by the Phillips Curve. I also generated various plots and outputs to visualize and interpret the results. These results have been documented, and I’ve ensured all key findings are clearly represented.

    Presentation Preparation:
    To accompany the analysis, I created a presentation that highlights the methodology, results, and interpretations. The presentation serves as a summary for discussions or evaluations and is ready for use.
    Now, my next step is to compile a detailed, cohesive report. This report will comprehensively describe my methodology, data preparation process, model specifications, analysis, and key findings. Additionally, I plan to include insights and discussions based on the models and visualizations I generated in gretl. 
    I want this report to effectively communicate the research process and results to a broader audience, potentially beyond those familiar with econometrics.
    I’d like help drafting and organizing this report, ensuring it is clear, detailed, and professional while reflecting the work I’ve done.
    
    Before proceeding with writing the detailed report, I plan to revisit the analysis I conducted earlier to ensure its robustness and potentially improve upon it. Here's my approach:

    Revisit Presentation and Results:
    I’ll begin by carefully reviewing the presentation I created and the results I previously generated. This step will help me identify any gaps, inconsistencies, or areas where further clarity or improvement is needed. It will also ensure that the key findings are aligned with the objectives of my project.

    Redo the Analysis in Gretl:
    After revisiting the results, I’ll redo the entire econometric analysis in Gretl. Since the data preparation process has already been completed and does not need to change, this step should be relatively quick. The focus will be on refining the models, improving the visualizations, and ensuring that the analysis is as thorough and accurate as possible.

    Prepare for the Report:
    Once the new analysis is complete, I’ll have updated results and insights that will form the foundation of the detailed report. With these in hand, I’ll proceed to write a comprehensive and professional document that reflects the improved analysis.

    By following this process, I aim to ensure that my final report not only communicates the work I’ve done but also stands out for its rigor and clarity.
    
    Analysis of the Presentation:
    Title:
    "The Relationship between Inflation and Unemployment: An Empirical Approach for the European Union Countries"

    Key Elements of the Study:
    Objective:
    The study examines the relationship between inflation and unemployment in European Union (EU) countries over the period 2000–2023, leveraging data from Eurostat. It seeks to demonstrate the inverse relationship between inflation and unemployment, as outlined by the Phillips Curve.

    Focus:
    The analysis centers on the short-run Phillips Curve, using the rate of wage growth as the dependent variable and the unemployment rate as the independent variable.

    Econometric Approach:

    Panel Data Model: The study employs Ordinary Least Squares (OLS) for a panel data framework.
    Diagnostic Tests: To validate the robustness of the model, the study conducts the following tests:
    White's Test for Heteroskedasticity: To check for uniform variability across variables.
    Distribution-free Wald Test: To examine common error variance across groups.
    Durbin-Watson Statistic: To detect residual autocorrelation.
    Hausman Test: To determine whether a fixed effects or random effects model is more appropriate.
    Models and Results:
    The presentation includes results for three model specifications:

    Pooled OLS Model
    Fixed Effects Model
    Random Effects Model
    The results are summarized in tables that include the constant term, unemployment rate coefficient, p-values, and R-squared values.
    Conclusion:
    The findings support the existence of an inverse relationship between unemployment and wage growth in EU countries during the study period (2000–2023), consistent with the short-run Phillips Curve.

    Visuals and Supporting Material:
    The presentation effectively incorporates diagrams and screenshots to support the analysis, including:

    Line Charts:
    Combined chart for all countries: "Average Annual Salary over Years" (created using Seaborn).
    Combined chart for all countries: "Unemployment Rate over Years" (created using Seaborn).
    Descriptive Statistics Tables:
    Table 1: Descriptive Statistics for 2000.
    Table 2: Descriptive Statistics for 2023.
    (Generated in Python and converted to LaTeX; code available upon request.)
    Gretl Screenshots:
    Model results: Pooled OLS using 624 observations.
    Panel model specifications.
    Plot:
    Gretl-generated plot: "Actual and Fitted Annual Salary Diff vs. Unemployment Rate."
    ''',

    "physiotherapy_app": '''
    I want to create an application that bridges the gap between physiotherapists and patients after treatment sessions. Often, patients either forget their home exercise routines or are unsure about performing them correctly. My app will act as a virtual guide, ensuring patients stay consistent and confident with their exercises.

    Here’s how it will work:

    1. Therapist-Driven Protocols: After a physiotherapy session, the therapist will set the exercise protocol in the app, including the type, frequency, repetitions, duration, and intensity of exercises. Patients won’t have access to modify these settings.

    2. Visual Guidance: Exercises will be explained using cartoon animations or clear diagrams to ensure patients understand every movement correctly.

    3. Reminders & Alerts: The app will send notifications to remind patients about their scheduled exercises, including any preparatory steps like applying a hot pack before starting.

    4. Exercise Categories: The app will have a library of exercises, including aerobic, resistance, range of motion (ROM), isometric, open-chain, and closed-chain kinematic exercises.

    5. Personalized Monitoring: The therapist can input specific health parameters, like heart rate targets, to ensure exercises are performed safely.

    6. Holistic Approach: The app won’t just focus on disease-specific protocols but will also include overall body conditioning plans.

    My goal is to make home exercise routines easy to follow, engaging, and safe, ultimately improving treatment outcomes and patient adherence.
    ''',
    
    "physiotherapy_research_help": '''
    I’m a final-year Physiotherapy student, and I’m currently searching for research articles that focus on recent advances in physiotherapy treatments from the year 2001 onward for the following conditions:

    Neurological conditions: Cerebral Palsy, Neural Tube Defects, Down Syndrome

    Musculoskeletal conditions: Osteoarthritis, Rheumatoid Arthritis, Amputation, Spondylosis, Degenerative Disc Disease, Prolapsed Intervertebral Disc

    Cardiopulmonary conditions: Pneumonia, Respiratory Distress Syndrome, Bronchitis, COPD, Asthma


    I’ve tried searching on Google Scholar, but most of the articles I found either had restricted access or only provided abstracts. I’m not sure how to access full-text articles or if there’s a specific platform or person I should approach for help with this. I’d really appreciate some guidance on how to effectively gather these resources.
    '''

}
