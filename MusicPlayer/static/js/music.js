player = document.getElementById('player')
current_time = document.getElementById('not_active_duration')
time_line_current = document.getElementById('active_duration')
sound_bar = document.getElementById('sound_bar')
footer_music_name = document.getElementById('footer_name_music')
loop = document.getElementById('loop')
let isLoop = false

player.addEventListener("ended", ()=>{
    if (isLoop) {
        player.currentTime = 0
        player.play()
    }
})

loop.addEventListener("click", ()=>{
    isLoop = !isLoop
    if(isLoop) {
        loop.style.backgroundColor = "white"
        loop.style.borderRadius = "50%"
    }
    if(!isLoop)
        loop.style.backgroundColor = "rgba(128, 128, 128, 0)"
})

function player_play(){
    player.play()
}

function player_pause(){
    player.pause()
}

function volume_change(){
    player.volume = sound_bar.value / 100
}

function update_timer(){
    time_line_current.style.width = player.currentTime / (player.duration / 100) + "%"
    if(time_line_current.style.width >= 100){
        clearTimeout(player_line_update)
    }
}
player_line_update = setInterval(update_timer, 10)

function play_this(event, name, author, url){
    player.setAttribute('src', url)
    footer_music_name.innerHTML = name
    let buttons = document.getElementsByClassName("play_btn")
    for (let button of buttons){
        button.style = "opacity: 0"
    }
    player.play()
}

function get_new_position(event){
    player.currentTime = my_map(event.pageX / (window.innerWidth / 100), 0, 100, 0, player.duration)
}

function my_map(x, in_min, in_max, out_min, out_max){
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
}

sound_bar.value = 50







