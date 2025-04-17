package io.github.some_example_name;


import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Input;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.utils.viewport.Viewport;

public class Player extends Sprite {

    private String filename = "dog.png";
    private float speed = 1.5f;
    private float velocityY = 0f; // velocity is speed + direction
    private final float gravity = -9.8f; // Adjust as needed
    private final float jumpVelocity = 5f; //  Adjust as needed
    private boolean isGrounded = true;


    public Player() {

        super(new Texture("dog.png"));
        setSize(1, 1);

    }

    void input(Viewport viewport) {
        float delta = Gdx.graphics.getDeltaTime(); // for all hw frame rate
        if (Gdx.input.isKeyPressed(Input.Keys.RIGHT) ||
            Gdx.input.isKeyPressed(Input.Keys.D)) {
            this.translateX(speed*delta);  // this == dog
        }
        if (Gdx.input.isKeyPressed(Input.Keys.LEFT) ||
            Gdx.input.isKeyPressed(Input.Keys.A)) {
            this.translateX(-speed*delta);
        }
        if (Gdx.input.isKeyJustPressed(Input.Keys.SPACE) && isGrounded) {
            velocityY = jumpVelocity;
            isGrounded = false;
            }
        velocityY += gravity * delta;
        this.translateY(velocityY * delta);
        if (this.getY() <= 0) {
            this.setY(0);
            velocityY = 0;
            isGrounded = true;
        }

// Check if you reached the ground at 0


        this.setX(MathUtils.clamp(this.getX(),
            0, viewport.getWorldWidth() - this.getWidth()));
    }

}
