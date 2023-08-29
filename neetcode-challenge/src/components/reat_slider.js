"use client"
import {useEffect,useState,useRef} from 'react'
import Card from './card'
import styles from '@/styles/slider.css'
import { motion } from "framer-motion"

const ReactSlider = ({list}) => {
    const myRef = useRef();

    useEffect(() => {
        const slider = document.querySelector('.items');
        let isDown = false;
        let startX;
        let scrollLeft;
    
        slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.classList.add('active');
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
        });
        slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.classList.remove('active');
        });
        slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.classList.remove('active');
        });
        slider.addEventListener('mousemove', (e) => {
        if(!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 3; //scroll-fast
        slider.scrollLeft = scrollLeft - walk;
        console.log(walk);
        });
    }, []);
    return (
        <motion.div className="items"
            // onMouseDown={(e) => mouseDownFn}
            // onMouseLeave={(e) => MouseLeaveFn}
            // onMouseUp={(e) => MouseUpFn}
            // onMouseMove={(e) => MouseMoveFn}
        >
            {list.map((item, index) => 
            {
                let bool=(index===0 || index===list.length-1)?false:true;
                return(
                    <motion.div 
                    ref={myRef}  
                    key={index}
                    className={`item ${index===list.length-1?'centerDiv':''}`}
                    initial={{opacity:0,y:-50}}
                    animate={{opacity:1,y:0}}
                    transition={{delay:1+(index*0.5), duration:1}}
                    >
                        {bool && <Card />}
                        {index===list.length-1 && <div><h3>See All</h3></div>}
                    </motion.div>
            )}
            )}
        </motion.div>
    )
}

export default ReactSlider