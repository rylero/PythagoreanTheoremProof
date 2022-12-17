from manim import *

class Main(Scene):
    def construct(self):
        tri = Polygon([-2,-1,0], [2,1,0], [2,-1,0]).set(z_index=3).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)

        cq = Polygon([-2,-1,0], [2,1,0], [0,5,0], [-4,3,0]).set_style(PURPLE_A, 0.1, PURPLE_C, stroke_opacity=1).set_z_index(2)
        bq = Polygon([2,-1,0], [-2,-1,0], [-2,-5,0], [2,-5,0]).set_style(GREEN_A, 0.1, GREEN_C, stroke_opacity=1).set_z_index(2)
        aq = Polygon([2,1,0], [2,-1,0], [4,-1,0], [4,1,0]).set_style(RED_A, 0.1, RED_C, stroke_opacity=1).set_z_index(2)

        a = Text("a").set_x(2.5).set_y(0)
        b = Text("b").set_x(0).set_y(-1.5)
        c = Text("c").set_x(0).set_y(0.5)

        a2 = Text("a^2").set_x(2.5).set_y(0)
        b2 = Text("b^2").set_x(0).set_y(-1.5)
        c2 = Text("c^2").set_x(0).set_y(0.5)
        
        g = VGroup()
        g.add(tri, cq, aq, bq, a, b, c, a2, b2, c2)
        g.scale(0.5)

        self.play(GrowFromCenter(tri))
        
        self.play(LaggedStart(
            GrowFromCenter(a), 
            GrowFromCenter(b), 
            GrowFromCenter(c), 
            lag_ratio=0.1)
        )

        self.wait(1)

        self.play(LaggedStart(
            GrowFromCenter(cq), 
            GrowFromCenter(aq), 
            GrowFromCenter(bq), 
            lag_ratio=0.1)
        )
        
        self.play(AnimationGroup(
            AnimationGroup(
                AnimationGroup(FadeOut(a), run_time=0.001),
                ApplyMethod(a2.move_to, aq.get_center())
            ),

            AnimationGroup(
                AnimationGroup(FadeOut(b), run_time=0.001),
                ApplyMethod(b2.move_to, bq.get_center())
            ),

            AnimationGroup(
                AnimationGroup(FadeOut(c), run_time=0.001),
                ApplyMethod(c2.move_to, cq.get_center())
            )
        ))
        self.wait(1)

        agroup = VGroup(aq, a2)
        bgroup = VGroup(bq, b2)
        cgroup = VGroup(cq, c2)

        self.play(
            AnimationGroup(FadeOut(tri), run_time=0),
            ApplyMethod(bgroup.move_to, [-4,0,0]),
            ApplyMethod(agroup.move_to, [-2.5,-1.5,0]),
            ApplyMethod(cgroup.move_to, [4,-0.5,0])
        )
        self.wait(1)
        
        tab1 = Polygon([-3,1,0], [-2,1,0], [-2,-1,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)
        tab2 = Polygon([-3,1,0], [-3,-1,0], [-2,-1,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)
        tab3 = Polygon([-5,-1,0], [-3,-1,0], [-3,-2,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)
        tab4 = Polygon([-5,-1,0], [-5,-2,0], [-3,-2,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)

        tc1 = Polygon([4.5,1.5,0], [5.5,1.5,0], [5.5,-0.5,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)
        tc2 = Polygon([5.5,-0.5,0], [5.5,-1.5,0], [3.5,-1.5,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)
        tc3 = Polygon([2.5,0.5,0], [2.5,-1.5,0], [3.5,-1.5,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)
        tc4 = Polygon([2.5,0.5,0], [2.5,1.5,0], [4.5,1.5,0]).set(z_index=1).set_style(BLUE_A, 0.1, BLUE_C, stroke_opacity=1)

        objectsToScale = [tab1, tab2, tab3, tab4, tc1, tc2, tc3, tc4, aq, bq, cq]
        for o in objectsToScale:
            o.scale(0.97)
        
        objectsToLower = [tc1, tc2, tc3, tc4]
        for o in objectsToLower:
            o.set_y(o.get_y()-0.5)

        self.play (LaggedStart(
            GrowFromCenter(tab1),
            GrowFromCenter(tab2),
            GrowFromCenter(tab3),
            GrowFromCenter(tab4),
            GrowFromCenter(tc1),
            GrowFromCenter(tc2),
            GrowFromCenter(tc3),
            GrowFromCenter(tc4), lag_ratio=0.1)
        )

        self.wait(0.2)

        label = Text("4(triangle) + a^2 + b^2 = 4(triangle) + c^2").set_x(0).set_y(2.5)
        label2 = Text ("a^2 + b^2 = c^2").set_x(0).set_y(1.75)

        l= Text("=").set_y(-0.5).set_x(0.25).scale(1.5)
        self.play(
            Write(l)
        )

        self.play(
            Write(label)
        )

        self.play(
            Write(label2)
        )

        self.wait()
        