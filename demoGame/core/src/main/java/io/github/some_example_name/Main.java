package io.github.some_example_name;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.math.Rectangle;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.FitViewport;
import com.badlogic.gdx.graphics.Color;
import com.badlogic.gdx.*;
import com.badlogic.gdx.audio.*;

import java.awt.*;

/** {@link com.badlogic.gdx.ApplicationListener} implementation shared by all platforms. */
public class Main implements ApplicationListener {

    // private Texture dogImage;
    private Texture background;
    private FitViewport viewport;
    private SpriteBatch spriteBatch;
    private Player dog;
    //private Sprite dog; -> changed to Player
    private Ball ball;
    private Sound bark;
    private float wait = 0f;


    @Override
    public void create() {
        // Prepare your application here.
        // dogImage = new Texture("dog.png");
        dog = new Player();
        //dog = new Sprite(dogImage);
        //dog.setSize(1, 1);
        ball = new Ball();
        background = new Texture("background-clouds.jpg");
        viewport = new FitViewport(8, 5);
        spriteBatch = new SpriteBatch();
        bark =  Gdx.audio.newSound(Gdx.files.internal("bark.mp3"));

    }

    @Override
    public void resize(int width, int height) {
        // Resize your application here. The parameters represent the new window size.
        viewport.update(width, height, true); // true centers the camera
    }

    @Override
    public void render() {
        onCollision();
        // Draw your application here.
        ScreenUtils.clear(Color.BLACK);
        //move();
        dog.input(viewport);
        ball.update(viewport);
        viewport.apply();
        spriteBatch.setProjectionMatrix(viewport.getCamera().combined);
        spriteBatch.begin();
        spriteBatch.draw(background, 0, 0,
            viewport.getWorldWidth(), viewport.getWorldHeight());
        dog.draw(spriteBatch);
        ball.draw(spriteBatch);
        spriteBatch.end();

    }
    public void onCollision() {
        Rectangle dogHitbox = dog.getBoundingRectangle();
        Rectangle ballHitbox = ball.getBoundingRectangle();
        if (dogHitbox.overlaps(ballHitbox)) {
            bark.play();
            System.out.println("BOUNCY BOING!");
            ball.rndmCollision(viewport);
        }

    }

    @Override
    public void pause() {
        // Invoked when your application is paused.
    }
    @Override
    public void resume() {
        // Invoked when your application is resumed after pause.
    }
    @Override
    public void dispose() {
        // Destroy application's resources here.
    }

//    private void input() {
//        float speed = 1.25f;
//        float delta = Gdx.graphics.getDeltaTime(); // for all hw frame rate
//        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT) ||
//            Gdx.input.isKeyPressed(Input.Keys.D)) {
//            dog.translateX(speed*delta);
//        }
//        if (Gdx.input.isKeyPressed(Input.Keys.LEFT) ||
//            Gdx.input.isKeyPressed(Input.Keys.A)) {
//            dog.translateX(-speed*delta);
//        }
//        dog.setX(MathUtils.clamp(dog.getX(),
//            0, viewport.getWorldWidth() - dog.getWidth()));
//    }

    public void move() {
        dog.translateX(.1f);// Move right
        dog.setX(MathUtils.clamp(dog.getX(),
            0, viewport.getWorldWidth() - dog.getWidth()));
    }
}

