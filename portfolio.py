import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header
st.write('''
# Shivam Sarkar
#####       Resume 
''')

image = Image.open('dp2.jpg')
st.image(image, width=140)

# SUMMARY

st.markdown('## Summary 📝', unsafe_allow_html=True)
st.info('''
- I’ve honed my skills in software development with a strong foundation in Python and API integration. My expertise in 
building Generative AI apps includes working with frameworks like Langchain and integrating both paid and open-source 
models such as OpenAI, Llama2, Mistral, and Gemini. I’m also knowledgeable about HuggingFace, Ollama, and Streamlit. 
My ongoing research on document similarity in Generative AI is enhancing my skills in statistical analysis and machine 
learning.

- Exploring the frontiers of Artificial Intelligence and Machine Learning at the National University of Singapore has 
profoundly deepened my understanding, especially in Explainable AI, which is crucial for building trust in AI 
applications. At the Institute of Engineering and Management, my research focuses on ecological recovery post-natural 
calamities using advanced data analytics, driven by a commitment to sustainable technologies.

- Proficient in leveraging technology to solve real-world problems, I’m eager to contribute to the Generative AI field 
and help build Retrieval Augmented Generation Models. I look forward to exploring collaborative opportunities in 
technology and AI. Let’s connect to discuss technology, innovation, or the latest in e-sports and gaming!
''')

#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<style>
/* Add styles for the navigation bar */
.navbar {
    transition: top 0s;
}

.hide-nav {
    top: -56px; /* Adjust this value based on your navbar height */
}

.show-nav {
    top: 0;
}

</style>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script>
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop) {
        navbar.classList.add('hide-nav');
        navbar.classList.remove('show-nav');
    } else {
        navbar.classList.add('show-nav');
        navbar.classList.remove('hide-nav');
    }
    lastScrollTop = scrollTop <= 0 ? 0 : scrollTop; // For Mobile or negative scrolling
});
</script>
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" target="_blank">Portfolio</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#achievements">Achievements</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Sections with Anchors

# EDUCATION

st.markdown('<a id="education"></a>', unsafe_allow_html=True)
st.markdown('## Education 🧠')
# Your education content here

st.write(
    '*Bachelor of Technology* (Computer Science, *Specialization in Artificial Intelligence*), **Institute of Engineering and Management**, Kolkata',
    'Year: 2021-2025')
st.markdown('''
- CGPA: `8.55`(Weighted Average)
''')

st.write(
    '*Senior School Certificate Examination* (Computer Science), **Techno India Group Public School (CBSE)**, Konnagar',
    'Year: 2021')
st.markdown('''
- Percentage: `90.0%`
''')

st.write('*Secondary School Examination* (Science), **Methodist School (ICSE)**, Dankuni',
         'Year: 2019')
st.markdown('''
- Percentage: `88.9%`
''')


# EXPERIENCE

st.markdown('<a id="experience"></a>', unsafe_allow_html=True)
st.markdown('## Experience 🚀')
# Your experience content here

# NATIONAL UNIVERSITY OF SINGAPORE
st.info('''**National University of Singapore** 

*Industrial Training Program (On-Site)*
        ''')
st.markdown('''
- Learned about the fundamentals of Artificial Intelligence, Machine Learning, Internet of Things and Data Analytics. 
- Comprehended *Explainable AI (XAI)* and it's importance for an organisation in building trust and confidence when putting 
AI Models into production, along with *Interpretable Model-Agnostic  Explanations (LIME)* and how it helps to eliminate a machine learning model and to make its predictions individually comprehensible.
''')

# INSTITUTE OF ENGINEERING AND MANAGEMENT
st.info('''**Institute of Engineering and Management** 

*Research Projects*
        ''')
st.markdown('''
- Post-Calamity Impact on Coastal Vegetation: Analyzing Shifts in Vegetation Indices in Google Earth Engine. 
- Generative AI for Document Similarity: A Comparative Analysis of Jaccard and Cosine Similarity with Time Complexity Insights.
''')

# PROJECTS

st.markdown('<a id="projects"></a>', unsafe_allow_html=True)
st.markdown('## Projects 💻')
# Your projects content here

# VERITEXT
st.info('''VeriText: Verify Authenticity in Every Line.''')
st.markdown('''Designed a cutting-edge web application to detect AI-generated text with precision and ease. Using Python and the Streamlit
framework, I created an intuitive user interface that seamlessly integrates with Langchain environment for advanced processing
. The application leverages the open-source Llama2 model to accurately differentiate between human-written and AI-generated content.
- Skills Used: Python, Streamlit, Langchain, Ollama''')
# INTELLITRIP
st.info('''IntelliTrip: Your Journey, Perfected by AI.''')
st.markdown('''
Developed an innovative AI-driven application that revolutionizes travel planning. IntelliTrip uses advanced artificial intelligence to generate personalized itineraries, 
accommodating user preferences and budget constraints. The application seamlessly integrates accommodation suggestions, activity recommendations, dining options, 
and transportation logistics, 
ensuring a well-rounded and stress-free travel experience.
- Skills Used: Python, Streamlit, Langchain, Ollama''')
# RAG PIPELINE
st.info('''Retrieval Augmented Generation(RAG) QnA ChatBot''')
st.markdown('''Developed} an advanced QnA ChatBot using the Langchain framework in Python, designed to retrieve and provide accurate information from user-supplied documents. 
The application leverages Retrieval-Augmented Generation (RAG) to enhance response precision and relevance, making it an invaluable tool for document-based queries.
- Skills Used: Python, Streamlit, Langchain, Ollama''')

# ACHIEVEMENTS

st.markdown('<a id="achievements"></a>', unsafe_allow_html=True)
st.markdown('## Achievements 🏆')
# Your achievements content here

st.info('''**Google Cloud Engineering**''')
st.markdown('''
- Learned about Cloud Architecture and Design. 
- Scaling computing resources using Google Compute Engine (VMs).
- Monitoring application performance and optimize cloud expenses. 
- Earned all the essential badges of Google Cloud Practitioners Programme. [`🔗`](https://www.cloudskillsboost.google/public_profiles/d8ff3599-749c-4799-a6eb-530539923e1b)
''', unsafe_allow_html=True)

st.info('''**Google Generative AI Study Jam**''')
st.markdown('''
- Developed Gen AI Applications with Gemini and Streamlit Frameworks.
- Prompt designing in Vertex AI.
- Earned all the essential badges of Google Gen AI Study Jam. [`🔗`](https://www.cloudskillsboost.google/public_profiles/f8746d60-6d37-4979-884c-7850a0c59196)
''', unsafe_allow_html=True)

st.info('''**IEM 2024 Aptitude Test (January)**''')
st.markdown('''
- **Achieved Rank 1** in the Aptitude Test conducted by IEM to assess cognitive abilities and skills.[`🔗`](https://drive.google.com/file/d/1HXTU6SuM7mzP_ozYGo8-oIm-NA2tAmEO/view?usp=sharing)
''', unsafe_allow_html=True)

st.info('''**VALORANT**''')
st.markdown('''
- As a semi-professional e-sports player, our team emerged as the sole champions, and the only team in South Asia to 
secure a **flawless victory** in Valorant Premiere Tournament 2024 
[`🔗`](https://tracker.gg/valorant/premier/standings?region=AP_SOUTH_ASIA&division=6&page=1&season=a1c4f86c-49fa-97bd-019b-aa8754ca7a83)
''', unsafe_allow_html=True)

# SKILLS

st.markdown('<a id="skills"></a>', unsafe_allow_html=True)
st.markdown('## Skills 🛠️')
# Your skills content here

st.markdown('''Programming: `Python`, `C`, `JAVA`''')
st.markdown('''Data processing/wrangling: `pandas`, `numpy`''')
st.markdown('''Data visualization: `matplotlib`, `seaborn`''')
st.markdown('''Natural Language Processing: `NLTK`, `SpaCy`''')
st.markdown('''Machine Learning: `scikit-learn''')
st.markdown('''Deep Learning', '`TensorFlow`''')
st.markdown('''Web development', '`Flask`, `Django`, `CSS`''')
st.markdown('''Model deployment: `Streamlit`, `gradio`, `Heroku`, `AWS`, `Langchain`, `Langsmith`''')

# SOCIAL MEDIA

st.markdown('<a id="social-media"></a>', unsafe_allow_html=True)
st.markdown('## Social Media 🌐')
# Your social media content here

st.markdown('''Email:- smsarkar2018@gmail.com''')
st.markdown('''LinkedIn:- https://www.linkedin.com/in/shivamsarkar''')
st.markdown('''GitHub:- https://github.com/sm-sarkar''')
