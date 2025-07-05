package io.github.some_example_name;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.math.MathUtils;
import com.badlogic.gdx.utils.viewport.Viewport;

public class Ball extends Sprite {

    private float speed = 1.5f;

    public Ball() {
        super(new Texture("ball.png"));
        setSize(1,1);

    }

    public void rndmCollision(Viewport viewport){
        float randomX = MathUtils.random(0,
            viewport.getWorldWidth() - this.getWidth());
        float randomY = MathUtils.random(0,
            viewport.getWorldHeight() - this.getHeight());
        this.setPosition(randomX, randomY);

    }

    public void update (Viewport v) {
        float delta = Gdx.graphics.getDeltaTime();
        if (this.getY() <= 0 || this.getY() >= v.getWorldHeight() - this.getHeight()) {
            speed = -speed; // reverse the direction at 0 (ground) & world height (top)
        }

        this.setX(MathUtils.clamp(this.getX(),
            0, v.getWorldWidth() - this.getWidth()));
        this.translate(speed*delta, speed*delta);
    }
}
