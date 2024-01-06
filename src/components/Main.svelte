<script>
    import Step from "./Step.svelte"

    let projects = [
        {name: 'This website', icon: 'fa-solid fa-globe', href: '#'},
        {name: 'Management app', icon: 'fa-solid fa-square-check', href: '#'},
        {name: 'Dotfiles', icon: 'fa-solid fa-terminal', href: '#'},
    ]
    
    let jobs = [
        {name: 'Data Science developer', icon: 'fa-solid fa-code'},
        {name: 'ML project mentor', icon: 'fa-solid fa-chalkboard-user'},
        {name: 'Math teacher', icon: 'fa-solid fa-school'},
    ]
    
    let skills = [
        {name: 'Programming Languages', icon: 'fa-regular fa-file-code'},
        {name: 'ML', icon: 'fa-solid fa-brain'},
        {name: 'Code Health', icon: 'fa-solid fa-book'},
        {name: 'Workflow', icon: 'fa-solid fa-gears'},
        {name: 'Web development technologies', icon: 'fa-solid fa-server'},
        {name: 'Languages', icon: 'fa-solid fa-language'},
    ]

    let hobbies = [
        {name: 'Playing chess', icon: 'fa-solid fa-chess'},
        {name: 'Playing with dogs', icon: 'fa-solid fa-dog'},
        {name: 'Learning', icon: 'fa-solid fa-graduation-cap'},
        {name: 'Reading', icon: 'fa-solid fa-book'},
    ]

    let benefits = [
        {name: 'An MLOps engineer', description: 'I have experience in all of the ML lifecycle, from designing a model to running and monitoring experiments and production inference. I have used all the classic frameworks and libraries in Python, and also some lesser known or less ML-centered ones, as discussed in the Tech section.'},
        {name: 'A DL engineer', description: 'I have worked a lot with Deep Neural Networks, especially in Natural Language Processing, though I also have some experience in Computer Vision. I have also had the opportunity to work on Large Language Models.'},
        {name: 'A self taught developer', description: 'I learnt how to code when I decided to switch from my position as a high school and university math teacher to the very promising field of Artificial Intelligence.<br /> Python has been the de facto language for Machine Learning for a few years now. This has led me to practice it a lot and fall in love with programming in general. I can design complex projects and review dense merge/pull requests in Python, ML related or not.<br /> I have collected a bunch of CS certifications that you can check out on my LinkedIn profile.'},
        {name: 'A software engineering enthousiast', description: 'I am very curious about everything related to software engineering. I entered this world with pure ML research in mind at first, but developed a passion for clean code, system design and workflow improvement. I always have one or two ongoing projects, hands-on or educational, and several others patiently waiting for their turn. While I firmly believe in specializing in specific areas, I also want a decent general knowledge of everything.'},
        {name: 'A passionate teacher', description: 'It started very early in my life. At 15 I was a teacher for my chess club and I managed to keep it going until I was 23. During my studies I was also a math private tutor. My first work experience was that of an actual math teacher (agrégé de mathématiques) in high school and university. Last but not least, as a second job, I am also working for a bootcamp company as a project mentor.'},
    ]
</script>

<main class="flex flex-col flex-1 p-4">
    <section id="intro-page" class="grid grid-cols-1 lg:grid-cols-2 gap-10 py-8 sm:py-14">
        <div class="flex flex-col lg:justify-center text-center lg:text-left gap-6 md:gap-8 px-4">
            <h2 class="font-semibold text-4xl sm:text-5xl md:text-6xl">
                Hi I'm <span class="ubuntu text-blue-800">Manu</span> Potrel<br />
                I'm an <span class="ubuntu text-blue-800">ML</span> Engineer<br />
                and a <span class="ubuntu text-blue-800">teacher</span>
            </h2>
            <p class="text-base sm:text-lg md:text-xl">
                My favorite <span class="text-blue-800">tech topics</span> include Deep Learning, Large Language Models/Large Multimodel Models and Software Engineering<br />
            </p>
            <a class="blueShadow mx-auto lg:mr-auto text-base sm:text-lg md:text-xl ubuntu relative overflow-hidden px-6 py-3 group rounded-full bg-white text-violet-400 cursor-pointer" href="https://www.linkedin.com/in/manuel-potrel-11903717b/" target="_blank">
                <div class="absolute top-0 right-full w-full h-full bg-violet-400 opacity-20 group-hover:translate-x-full z-0 duration-200"></div>
                <h4 class="relative z-9">Get in touch &rarr;</h4>
            </a>
        </div>
        <div class="relative grid place-items-center">
            <img src={"images/mewithguigui-nobg.png"} alt="Profile image" class="object-cover z-[2] max-h-[70vh]" />
        </div>
    </section>
    
    
    <section id="about" class="py-20 pt-10 lg:pt-16 lg:py-32 flex flex-col gap-16 sm:gap-20 md:gap-24 relative">
        <div class="flex flex-col gap-2 text-center relative before:absolute before:top-0 before:left-0 before:w-2/3 before:h-1.5 before:bg-violet-700 after:absolute after:bottom-0 after:right-0 after:w-2/3 after:h-1.5 after:bg-violet-700 py-4">
            <h6 class="text-lg sm:text-xl md:text-2xl">Want to know more?</h6>
            <h3 class="font-semibold text-3xl sm:text-4xl md:text-5xl">A bit <span class="ubuntu text-blue-600">about</span> me.</h3>
        </div>
        <p class="mx-auto ubuntu font-semibold text-lg sm:text-xl md:text-2xl">I am . . .</p>
        <div class="flex flex-col gap-20 w-full mx-auto max-w-[800px]">
            {#each benefits as benefit, index}
            <div class="flex gap-6 sm:gap-8">
                <p class="ubuntu text-4xl sm:text-5xl md:text-6xl text-amber-600 font-semibold">
                    0{index+1}
                </p>
                <div class="flex flex-col gap-6 sm:gap-8">
                    <h3 class="text-2xl sm:text-3xl md:text-5xl">
                        {benefit.name}
                    </h3>
                    <p>{@html benefit.description}</p>
                </div>
            </div>
            {/each}
        </div>
    </section>



    <section id="experience" class="py-20 pt-10 lg:pt-16 lg:py-32 flex flex-col gap-16 sm:gap-20 md:gap-24 relative">
        <div class="flex flex-col gap-2 text-center relative before:absolute before:top-0 before:left-0 before:w-4/5 before:h-1.5 before:bg-violet-700 after:absolute after:bottom-0 after:right-0 after:w-4/5 after:h-1.5 after:bg-violet-700 py-4">
            <h6 class="text-lg sm:text-xl md:text-2xl">Resume</h6>
            <h3 class="font-semibold text-3xl sm:text-4xl md:text-5xl">Relevant <span class="ubuntu text-blue-600">work experiences</span></h3>
        </div>
        <p class="mx-auto ubuntu font-semibold text-lg sm:text-xl md:text-2xl">I have worked as a . . .</p>
        <div class="grid grid-cols-1 gap-12 lg:gap-10">
            <Step step={jobs[0]}>
                <ul>
                    <li><strong>(2021 - ) Sancare</strong></li>
                </ul>
                <p>
                    I have been a Data Science developer at Sancare, a french company working with hospitals to help them categorize patient stays using NLP and structured data, and with pharmaceutical companies to run statistical studies.
                </p>
                <ul>
                    <li>I have helped develop and design an LLM repository for entity extractions in pharmaceutical studies</li>
                    <li>I have built components of the ML stack, reviewed critical packages and I have been involved in refactoring several key parts of the main ML packages</li>
                    <li>I have run experiments to improve the performance of our NLP models</li>
                    <li>I have monitored, debugged and maintained our ML services on the hospital prod servers</li>
                </ul>
            </Step>
            <Step step={jobs[1]}>
                <ul>
                    <li><strong>(2023 - ) DataScientest</strong></li>
                </ul>
                <p>
                    This was the bootcamp company I chose to learn about Data Science, so it meant a lot to me when they reached out to ask if I would be willing to mentor new learners. Obviously, I immediately accepted.<br />
                    I have been mentoring several projects based on story telling, data analysis, feature engineering and Deep Learning.<br />
                    One of the most wonderful aspects of this job is that I have had many groups so far from different countries, so this has been (and keeps being) an incredible experience!
                </p>
            </Step>
            <Step step={jobs[2]}>
                <ul>
                    <li><strong>(2017 - 2018) Lycée François 1er</strong></li>
                    <li><strong>(2018 - 2021) Lycée Galilée</strong></li>
                    <li><strong>(2019 - 2021) CYU university</strong></li>
                </ul>
                <p>
                    I have given math lessons in university and engineering school, and I have been a match teacher in high school for over four years, where I had to learn how to communicate with a sometimes difficult audience of heterogenous levels (believe it or not, teaching those sometimes difficult teenagers has actually been one of the most enjoyable time of my career).
                    I have also given some basic high school computer science courses during my time as a teacher.
                </p>
            </Step>
        </div>
    </section>



    <section id="skills" class="py-20 pt-10 lg:pt-16 lg:py-32 flex flex-col gap-16 sm:gap-20 md:gap-24 relative">
        <div class="flex flex-col gap-2 text-center relative before:absolute before:top-0 before:left-0 before:w-11/12 before:h-1.5 before:bg-violet-700 after:absolute after:bottom-0 after:right-0 after:w-11/12 after:h-1.5 after:bg-violet-700 py-4">
            <h6 class="text-lg sm:text-xl md:text-2xl">Technical toolbox</h6>
            <h3 class="font-semibold text-3xl sm:text-4xl md:text-5xl"><span class="ubuntu text-blue-600">Languages and frameworks</span> knowledge</h3>
        </div>
        <p class="mx-auto ubuntu font-semibold text-lg sm:text-xl md:text-2xl">I have experience with . . .</p>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-10">
            <Step step={skills[0]}>
                <ul>
                    <li><strong>Proficient</strong>: Python</li>
                    <li><strong>Decent</strong>: Rust</li>
                    <li><strong>WIP</strong>: Javascript, Typescript, C</li>
                    <li><strong>Coming soon</strong>: C++, Golang, Haskell, Lua</li>
                </ul>
            </Step>
            <Step step={skills[1]}>
                <ul>
                    <li><strong>Machine Learning</strong>: pandas/polars, numpy, seaborn, scikit-learn, mlflow</li>
                    <li><strong>ML Ops</strong>: Monitoring, evaluating, fine tuning, investigating</li>
                    <li><strong>Deep Learning</strong>: tensorflow, torch, skorch, transformers</li>
                    <li><strong>LLM</strong>: transformers, langchain, rellm</li>
                </ul> 
            </Step>
            <Step step={skills[2]}>
                <ul>
                    <li><strong>Books read</strong>: Clean Code, Head First Design Patterns</li>
                    <li><strong>Certifications</strong>: The Software Designer Mindset</li>
                    <li><strong>Coming soon</strong>: The Software Architect Mindset, Grokking Concurrency</li>
                </ul>
            </Step>
            <Step step={skills[3]}>
                <ul>
                    <li><strong>Code editors</strong>: NeoVim, Helix, VS Code, PyCharm</li>
                    <li><strong>OS</strong>: Ubuntu, MacOs, ArchLinux, Windows</li>
                    <li><strong>Shell & Terminal</strong>: Kitty/Alacritty, Zsh, Tmux</li>
                </ul>
            </Step>
            <Step step={skills[4]}>
                <ul>
                    <li><strong>Known languages</strong>: HTML, CSS, Javascript</li>
                    <li><strong>Known frameworks/libraries</strong>: React (barely), Svelte (OK)</li>
                    <li><strong>Used once or twice</strong>: PHP, Nginx</li>
                </ul>
            </Step>
            <Step step={skills[5]}>
                <ul>
                    <li><strong>Native</strong>: French</li>
                    <li><strong>Professional</strong>: English</li>
                    <li><strong>High school (so please don't)</strong>: German</li>
                </ul>
            </Step>
        </div>
    </section>


    <section id="projects" class="py-20 lg:py-32 flex flex-col gap-24">
        <div class="flex flex-col gap-2 text-center">
            <h6 class="text-lg sm:text-xl md:text-2xl">
                A few of my personal projects.
            </h6>
            <h3 class="font-semibold text-3xl sm:text-4xl md:text-5xl">
                Curious to <span class="ubuntu text-blue-800">see</span> my projects?
            </h3>
        </div>
        <a href="https://github.com/mpotrel" target="_blank" class="bg-white mx-auto px-4 py-2 rounded-md border border-solid border-violet-400 flex items-center gap-2 -mb-4 sm:-mb-0 -mt-10 hover:border-violet-700 duration-200">
            <i class="fa-brands fa-github"></i>
            <p>My github page</p>
        </a>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-12 lg:gap-10">
            <Step step={projects[0]}>
                <p>
                    This website was created using <span class="ubuntu text-blue-600"></span>Svelte with <span class="ubuntu text-blue-600">Tailwind CSS</span>. I wanted to learn about some web technologies, being already somewhat familiar with <span class="ubuntu text-blue-600">HTML</span>, <span class="ubuntu text-blue-600">CSS</span> and <span class="ubuntu text-blue-600">JavaScript</span>, so I thought "why not use one of the current cool kids' framwork?".
                </p>
            </Step>
            <Step step={projects[1]}>
                <p>
                    (Coming soon) I had been trying to learn <span class="ubuntu text-blue-600">Rust</span> for a few weeks when I decided to follow <a class="ubuntu text-blue-600" href="https://www.youtube.com/c/theprimeagen">ThePrimeagen</a>'s advice to start by building something I need. And while I do love <span class="ubuntu text-blue-600">Obsidian</span>, I thought building a custom task management and note taking app would be both challenging and instructive.
                </p>
            </Step>
            <Step step={projects[2]}>
                <p>
                    My most important config files.<br />
                    Workflow improvement has basically become a hobby. I am primarily working on an <span class="ubuntu text-blue-600">Ubuntu</span> OS, <span class="ubuntu text-blue-600">MacOS</span> being a close second, and occasionally <span class="ubuntu text-blue-600">Arch</span> as well.<br />
                    Most of my workflow is keyboard and terminal based.
                </p>
            </Step>
        </div>
    </section>


    <section id="hobbies" class="py-20 pt-10 lg:pt-16 lg:py-32 flex flex-col gap-16 sm:gap-20 md:gap-24 relative">
        <div class="flex flex-col gap-2 text-center relative before:absolute before:top-0 before:left-0 before:w-2/3 before:h-1.5 before:bg-violet-700 after:absolute after:bottom-0 after:right-0 after:w-2/3 after:h-1.5 after:bg-violet-700 py-4">
            <h6 class="text-lg sm:text-xl md:text-2xl">When work is over</h6>
            <h3 class="font-semibold text-3xl sm:text-4xl md:text-5xl">My <span class="ubuntu text-blue-600">hobbies</span></h3>
        </div>
        <p class="mx-auto ubuntu font-semibold text-lg sm:text-xl md:text-2xl">I love spending time . . .</p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-10">
            <Step step={hobbies[0]}>
            </Step>
            <Step step={hobbies[1]}>
            </Step>
            <Step step={hobbies[2]}>
            </Step>
            <Step step={hobbies[3]}>
            </Step>
        </div>
    </section>
</main>
