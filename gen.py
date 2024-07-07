images = [ 
           {"file":"IMG_5964.JPG", "id":"10674","size":"16x12"},
           {"file":"IMG_5966.JPG", "id":"34982","size":"16x12"},
           {"file":"IMG_5984.JPG", "id":"08219","size":"10x8"},
           {"file":"IMG_5967.JPG", "id":"61034","size":"24x30"},
           {"file":"IMG_5985.JPG", "id":"59281","size":"16x12"},
           {"file":"IMG_5998.JPG", "id":"01954","size":"8x10"},
           {"file":"IMG_5970.JPG", "id":"70291","size":"16x12"},
           {"file":"IMG_5986.JPG", "id":"48307","size":"10x8"},
           {"file":"IMG_5971.JPG", "id":"39512","size":"20x16"},
           {"file":"IMG_5987.JPG", "id":"15940","size":"15x11"},
           {"file":"IMG_5988.JPG", "id":"02837","size":"10x8"},
           {"file":"IMG_5976.JPG", "id":"87564","size":"16x12"},
           {"file":"IMG_5989.JPG", "id":"54120","size":"10x8"},
           {"file":"IMG_5977.JPG", "id":"74059","size":"20x16"},
           {"file":"IMG_5990.JPG", "id":"49012","size":"10x8"},
           {"file":"IMG_5978.JPG", "id":"32185","size":"16x12"},
           {"file":"IMG_20240602_140150074.jpg", "id":"06948","size":"10x8"},
           {"file":"IMG_5991.JPG", "id":"23097","size":"10x8"},
           {"file":"IMG_5979.JPG", "id":"81230","size":"16x12"},
           {"file":"IMG_5992.JPG", "id":"57481","size":"10x8"},
           {"file":"IMG_5980.JPG", "id":"02836","size":"16x12"},
           {"file":"IMG_5993.JPG", "id":"50947","size":"10x8"},
           {"file":"IMG_20240602_140719427.jpg", "id":"16238","size":"7x5"},
           {"file":"IMG_5981.JPG", "id":"39184","size":"16x12"},
           {"file":"IMG_5994.JPG", "id":"67902","size":"10x8"},
           {"file":"IMG_20240602_141216933.jpg", "id":"84751","size":"28x22"},
           {"file":"IMG_5995.JPG", "id":"72094","size":"7x5"},
           {"file":"IMG_5965.JPG", "id":"06325","size":"16x12"},
           {"file":"IMG_5983.JPG", "id":"18402","size":"10x8"},
           {"file":"IMG_5996.JPG", "id":"45093","size":"8x10"},
           {"file":"IMG_5984.JPG", "id":"03941","size":"10x8"},
           {"file":"IMG_6000.JPG", "id":"57126","size":"7x5"},
           {"file":"IMG_6001.JPG", "id":"29834","size":"12x9"},
           {"file":"IMG_6002.JPG", "id":"96207","size":"20x18"},
           {"file":"IMG_6003.JPG", "id":"05123","size":"10x7"},
           {"file":"IMG_6004.JPG", "id":"48309","size":"10x8"},
           {"file":"IMG_6007.JPG", "id":"21684","size":"18x24"},
           {"file":"IMG_6009.JPG", "id":"35871","size":"8x10"},
           {"file":"IMG_20240602_124140197.jpg", "id":"49028","size":"8x10"},
           {"file":"IMG_20240602_140048052.jpg", "id":"80346","size":"11x14"},
           {"file":"IMG_20240602_140112161.jpg", "id":"00146","size":"4x6"},
           {"file":"IMG_5975.JPG", "id":"00199","size":"16x20"},
           {"file":"IMG_20240602_140141736.jpg", "id":"00200","size":"8x10"}
         ]

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{IMAGE_ALT}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow: hidden;
        }}
        .content {{
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        img {{
            max-width: 100%;
            max-height: 90vh;
        }}
        .navigation {{
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
        }}
        .timer {{
            font-size: 0.8em;
            margin-left: 10px;
        }}
    </style>
    <script>
        let timer;
        let pauseTimeout;
        let countdownInterval;
        let countdown = 60;
        let isPaused = false;

        function startSlideshow() {{
            timer = setInterval(nextImage, 5000);
        }}

        function nextImage() {{
            window.location.href = "{NEXT_IMAGE}";
        }}

        function manualAdvance() {{
            clearInterval(timer);
            clearTimeout(pauseTimeout);
            resetPauseTimer();
            nextImage();
        }}

        function pauseSlideshow() {{
            if (isPaused) {{
                isPaused = false;
                startSlideshow();
                clearInterval(countdownInterval);
                document.getElementById('countdown').style.display = 'none';
            }} else {{
                clearInterval(timer);
                clearInterval(countdownInterval);
                isPaused = true;
                countdown = 60;
                updateCountdown();
                countdownInterval = setInterval(updateCountdown, 1000);
                pauseTimeout = setTimeout(() => {{
                    isPaused = false;
                    startSlideshow();
                    clearInterval(countdownInterval);
                    document.getElementById('countdown').style.display = 'none';
                }}, 60000);
            }}
        }}

        function resetPauseTimer() {{
            clearTimeout(pauseTimeout);
            pauseTimeout = setTimeout(() => {{
                isPaused = false;
                startSlideshow();
                clearInterval(countdownInterval);
                document.getElementById('countdown').style.display = 'none';
            }}, 60000);
        }}

        function updateCountdown() {{
            const countdownElement = document.getElementById('countdown');
            const minutes = Math.floor(countdown / 60);
            const seconds = countdown % 60;
            countdownElement.textContent = `${{minutes}}:${{seconds.toString().padStart(2, '0')}}`;
            countdownElement.style.display = countdown > 0 ? 'inline' : 'none';
            if (countdown > 0) {{
                countdown--;
            }} else {{
                clearInterval(countdownInterval);
            }}
        }}

        function toggleFullscreen() {{
            if (!document.fullscreenElement) {{
                document.documentElement.requestFullscreen();
            }} else {{
                if (document.exitFullscreen) {{
                    document.exitFullscreen();
                }}
            }}
        }}

        document.addEventListener('DOMContentLoaded', (event) => {{
            startSlideshow();
            document.addEventListener('keydown', (event) => {{
                if (event.code === 'Space') {{
                    pauseSlideshow();
                }}
            }});
        }});
    </script>
</head>
<body>
    <div class="content">
        <img src="{IMAGE_SRC}" alt="{IMAGE_ALT}">
    </div>
    <div class="navigation">
        {IMAGE_ALT} {SIZE} |
        <a href="{PREV_IMAGE}">Previous</a> |
        <a href="../index.html">Index</a> |
        <a href="{NEXT_IMAGE}" onclick="manualAdvance(); return false;">Next</a> |
        <a href="#" onclick="toggleFullscreen(); return false;">Full-Screen</a>
        <a href="#" onclick="pauseSlideshow(); return false;">Pause</a> |
        <span id="countdown" class="timer"></span>
    </div>
</body>
</html>
"""

for i, image in enumerate(images):
    prev_image = f"{images[i-1]['file'].replace('.JPG','').replace('.jpg','')}.html" if i > 0 else f"{images[-1]['file'].replace('.JPG','').replace('.jpg','')}.html"
    next_image = f"{images[i+1]['file'].replace('.JPG','').replace('.jpg','')}.html" if i < len(images) - 1 else f"{images[0]['file'].replace('.JPG','').replace('.jpg','')}.html"
    base = image["file"].replace(".JPG", "").replace(".jpg", "")

    html_content = template.format(
        IMAGE_ALT=image['id'],
        SIZE=image['size'],
        IMAGE_SRC=image['file'],
        PREV_IMAGE=prev_image,
        NEXT_IMAGE=next_image
    )

    with open(f"images/{base}.html", "w") as file:
        file.write(html_content)

