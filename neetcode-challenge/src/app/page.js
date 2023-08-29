"use client"
import React from 'react'
import SectionOneLeft from '@/components/sectionOneLeft'
import SectionOneRight from '@/components/sectionOneRight'
import styles from '@/styles/Home.module.css'
import ReactSlider from '@/components/reat_slider'
import { motion } from "framer-motion"
import DataStructureTabs from '@/components/dataStructureTabs'

const Homepage = () => {
    return (
        
        <div >
            {/* Main page */}
            <div className={`${styles.section1} ${styles.treeRoot}`}>
                <div className={`${styles.mainPage}` }>
                    <SectionOneLeft />
                    <SectionOneRight />
                </div>

                <motion.div className={styles.subDetails}
                    initial={{opacity:0,y:-50}}
                    animate={{opacity:1,y:0}}
                    transition={{delay:1, duration:1}}>
                    <h3>Its a challenge of 150 programs to solve on all different data structure topics.<br></br>
            These question are frequently asked in the interviews.</h3>
                </motion.div>

                <div className={`${styles.sizedBox}`} style={{height:150}}></div>
            </div>

            {/* Cards */}
            <div className={`${styles.section2}  ${styles.treeRoot}`}>
                <div className={styles.cardList}>    
                <ReactSlider list={[1,2,4,6,2,4,5,6]}></ReactSlider>
                </div>  
            </div>

            {/* Tabs */}
            <div className={`${styles.section3}  ${styles.treeRoot}`}>
            <DataStructureTabs tabs={['Array','Searching','Trees','List','Dynamic Programming'] }></DataStructureTabs>
            </div>

        </div>
    )
}

export default Homepage