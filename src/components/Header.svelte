<script>
    export let y;
    let tabs = [
        {name: "About me", link: "#about"},
        {name: "Work experience", link: "#experience"},
        {name: "Skills", link: "#skills"},
        {name: "Projects", link: "#projects"},
        {name: "Hobbies", link: "#hobbies"},
    ]
</script>

<header 
    class={'sticky z-[10] top-0 duration-200 px-6 flex items-center justify-between border border-solid ' + (
        y > 0 ? 'py-4 bg-blue-100 border-violet-600': 'py-p6 bg-transparent border-transparent'
    )}
>
    <h1 class="font-medium">
        <img src={"images/roboy2.png"} class="w-auto h-24 px-8" alt="logo" />
        <!-- <b class="font-bold ubuntu">Manu</b> Potrel's resume -->
    </h1>
    <div class="sm:flex ml-auto pr-4 items-center gap-4 hidden">
        {#each tabs as tab, index}
            <a class="duration-200 hover:text-violet-400" href={tab.link}>
                <p class="font-bold">{tab.name}</p>
            </a>
        {/each}
    </div>
    <a class="blueShadow relative overflow-hidden px-5 py-2 group rounded-full bg-white text-amber-800" href="https://www.linkedin.com/in/manuel-potrel-11903717b/" target="_blank">
        <div class="absolute top-0 right-full w-full h-full bg-violet-400 opacity-20 group-hover:translate-x-full z-0 duration-200"></div>
        <h4 class="relative z-9">Get in touch</h4>
    </a>
</header>