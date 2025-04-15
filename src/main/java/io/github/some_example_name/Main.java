package io.github.some_example_name;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.utils.ScreenUtils;
import com.badlogic.gdx.utils.viewport.FitViewport;
import com.badlogic.gdx.graphics.Color;

import java.awt.*;

/** {@link com.badlogic.gdx.ApplicationListener} implementation shared by all platforms. */
public class Main implements ApplicationListener {

    private Texture dogImage;
    private Texture background;
    private FitViewport viewport;
    private SpriteBatch spriteBatch;
    private Sprite dog;
    private float fTimeElapsed = 0;
    private boolean bMovingRight = true;
    private boolean bReturningToCenter = false;
    private boolean bStopAtCenter = false;


    @Override
    public void create() {
        // Prepare your application here.
        dogImage = new Texture("dog.png");
        dog = new Sprite(dogImage);
        dog.setSize(1, 1);
        background = new Texture("background-clouds.jpg");
        viewport = new FitViewport(8, 5);
        spriteBatch = new SpriteBatch();

    }

    @Override
    public void resize(int width, int height) {
        // Resize your application here. The parameters represent the new window size.
        viewport.update(width, height, true); // true centers the camera
    }

    @Override
    public void render() {
        // Draw your application here.
        ScreenUtils.clear(Color.BLACK);
        move();
        viewport.apply();
        spriteBatch.setProjectionMatrix(viewport.getCamera().combined);
        spriteBatch.begin();
        spriteBatch.draw(background, 0, 0,
            viewport.getWorldWidth(), viewport.getWorldHeight());
        dog.draw(spriteBatch);
        spriteBatch.end();
        fTimeElapsed += com.badlogic.gdx.Gdx.graphics.getDeltaTime();
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

    public void move() {
        float fMiddleX = (viewport.getWorldWidth() - dog.getWidth()) / 2; // Pinpoints center of screen (where he stops)
        float fRightEdge = viewport.getWorldWidth() - dog.getWidth(); // Far right edge- where he pivots back

        if (!bStopAtCenter) {  // if he is moving
            if (bMovingRight) {  // if he is moving RIGHT
                dog.translateX(0.025f);  // movement to the right & speed
                if (dog.getX() >= fRightEdge) {  // when he reaches right side...
                    dog.setX(fRightEdge);
                    bMovingRight = false;  // stop going right and...
                    bReturningToCenter = true; // send him to the MIDDLE!
                }
            } else if (bReturningToCenter) {
                dog.translateX(-0.025f);  // movement back to CENTER
                if (dog.getX() <= fMiddleX) {
                    dog.setX(fMiddleX); // Hops back to center screen
                    bStopAtCenter = true; // Stops moving (stays hoppin' though!)
                }
            }
        }

        float fHopHeight = 0.5f;  // how high he hops
        float fHopSpeed = 8f;  //  how fast he hops
        dog.setY((float)Math.sin(fTimeElapsed * fHopSpeed) * fHopHeight);  // 'sine wave' creates animated hop
    }

}
