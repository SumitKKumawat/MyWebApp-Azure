"""
Summary
-------
The summary is a brief intro. You can put raw HTML into this field.
"""
summary = '<p> A seasoned Software professional with over 7 years of rich experience in Artificial Intelligence, Machine Learning and Robotics Automation. Responsible for Continous Improvement and Business Digital Trasnformation. </p>'

languages = [
        ['Hindi', ' (Native)'],
        ['English', ' (Proffesional)']
        ]

education = [
        ['Computer Science', 'Maharshi Arvind Inst. of Sc. & Mgmt.', '2010 - 2013'],
        ['Udacity', '2020 - 2020']
        ]

interests = ['Farming', 'Badminton', 'Cooking']

skills = [
        ['Python & Django', '98%'],
        ['Azure', '95%'],
        ['VBA', '99%'],
        ['Machine Learning', '96%'],
        ['Computer Vision', '90%'],
        ['Sketch & Photoshop', '60%']
        ]

"""
Experience
----------
This should be a list of lists. Each sublist corresponds to a particular job
and is of the form:
    ['Title', 'Date range', 'Company name and location', 'Description of role']

The 'Description of role' field does not get escaped by the templating engine,
so you can put raw HTML in it if you like.
"""
experience = [
        ['Robotics Developer',
            '2019 - Present',
            'Tesco, India',
            '<p>Describe your role here lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo.</p>  <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. </p>'
        ],
        ['Automation Analyst',
            '2017 - 2019',
            'Tesco, India',
            '<p>Describe your role here lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.</p>'
        ],
        ['Analyst',
            '2013 - 2017',
            'Genpact, India',
            '<p>Describe your role here lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.</p>'
        ]
    ]

"""
Projects
--------
The project_intro field is for a short introduction to your work.
Project are a list of lists, where each sublist refers to a specific project,
and is of the form:
    ['Title', 'Description', 'Link to project webpage']
"""
project_intro = '<p>You can list your side projects or open source libraries in this section. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et ligula in nunc bibendum fringilla a eu lectus.</p>'
projects = [
        ['Velocity',
            'A responsive website template designed to help startups promote, market and sell their products.',
            '#hook'
        ],
        ['DevStudio',
            'A responsive website template designed to help startups promote, market and sell their products.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-web-development-agencies-devstudio/'
        ],
        ['Tempo',
            'A responsive website template designed to help startups promote their products or services and to attract users &amp; investors.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-startups-tempo/'
        ],
        ['Atom',
            'A comprehensive website template solution for startups/developers to market their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-mobile-apps-atom/'
        ],
        ['Delta',
            'A responsive Bootstrap one page theme designed to help app developers promote their mobile apps.',
            'http://themes.3rdwavemedia.com/website-templates/responsive-bootstrap-theme-for-mobile-apps-delta/'
        ]
    ]



"""
default_data
------------
This dictionary puts everything together. It will be read by the Flask app when
it is instantiated.
"""
default_data = {
    'site_title' : 'Meet your AI Professional',
    'name' : 'Sumit K',
    'tagline' : 'Robotics Developer',
    'email' : 'contact@sumeet.ai',
    'phone' : '0123 456 789',
    'website' : 'www.sumeet.ai',
    'linkedin' : 'https://www.linkedin.com/in/sumit-k-kumawat/',
    'github' : 'github.com/sumit-k-kumawat',
    'twitter' : '@twittername',
    'languages' : languages,
    'education' : education,
    'interests' : interests,
    'skills' : skills,
    'summary' : summary,
    'experience' : experience,
    'project_intro' : project_intro,
    'projects' : projects
    }
