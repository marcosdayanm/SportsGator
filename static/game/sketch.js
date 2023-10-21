
let balls = [];
let ballCount = 0;
let lives = 5;
let speed = 1;
let bg;
let ballImg;


// Clase paa crear nuevos balones
class Ball
{
  
  constructor(x, y, sizex, sizey, color, speed)
  {
    this.x = x;
    this.y = y;
    this.sizex = sizex;
    this.sizey = sizey;
    this.color = color;
    this.speed = speed;
  }
  
  // se puede el nombre que sea pero por convención
  draw() {
    
    
    fill(this.color) // también se podría hacer con rgb, y cambiar las intensidades
    stroke(1)

    //ellipse(this.x, this.y, this.sizey, this.sizex) //parametros x, y, h, w
    
    image(ballImg, this.x - this.sizex/2 - 10, this.y - this.sizey/2, this.sizex*2, this.sizey);


    this.y+= this.speed;

  } // draw
  
  hit(x, y)
  {
    // console.log("x:", x, "y:", y, "this.x:", this.x, "this.y:", this.y);
    let d = dist(x, y, this.x, this.y);
    if (d <= this.sizex)
    {
      return true;
    }
    return false;
  }
} // class


function preload() {
  bg = loadImage('../static/game/field.png');
  ballImg = loadImage('../static/game/ball_wo_bg.png');
}





// start
function setup() {
  // función para crear canvas de cierto tamaño
  createCanvas(600, 600);
}


function drawMouse()
{
  fill('rgba(255,0,0,0.18)');
  stroke('rgba(255,0,0,0)')
  ellipse(mouseX, mouseY, 10, 10)
}


function drawText()
{
  fill(0);
  textSize(24);
  text(`Score: ${ballCount}`, 10, 25);
  
  text(`Lives: ${lives}`, 505, 25);
}




// loop, ciclo infinito que corre mientras la app corre
function draw() 
{

  
  background('rgb(202,255,202)'); // si se pone solo un número, se asume que todos los colores de rgb van a tener ese valor
  
  image(bg, 0, 0, width, height);
  
  drawText();
  
  if(frameCount % 45 == 0)
  {
    if (balls.length > 3)
    {
      if(frameCount % 90 == 0)
        {
          let ball = new Ball(random(20, width-20), -13, 25, 50, '#CC9C39', speed);
    balls.push(ball);
        }
    }
    else
    {
      let ball = new Ball(random(20, width-20), -13, 25, 50, '#CC9C39', speed);
      balls.push(ball);
    }

    
  }
  
  // dibuja los balones
  for(let i = balls.length - 1; i>=0; i--)
    {
      balls[i].draw();
    
      if (balls[i].y > height + 20)
        {
          // console.log("Ball out of bounds", balls[i].y);
          lives --;
          balls.splice(i, 1)
          continue;
        }
      
      if (balls[i].hit(mouseX, mouseY))
        {
          balls.splice(i, 1)
          ballCount++;
          
          if (speed < 6){
            speed += 0.06;
          }
          speed += 0.04;
          continue;
        }
    }
  
  
  // parar el loop si ya se llegó a 0 vidas
  if (lives <= 0) {
    textSize(64);
    fill(255)
    rect(width/2 - 195, height/2 - 115, 400, 80, 40);
    fill(255, 0, 0);
    text("Game Over", width/2 - 160, height/2 - 55);
    noLoop(); // Detiene la ejecución de draw()
  }
  
  drawMouse();
}

