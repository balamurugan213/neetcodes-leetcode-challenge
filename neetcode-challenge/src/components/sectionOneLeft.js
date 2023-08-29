"use client"
import React from 'react'
import styles from '@/styles/Home.module.css'
import {motion} from 'framer-motion'

const SectionOneLeft = () => {
  return (
    <motion.div className={styles.branch1}
    initial={{opacity:0,y:-50}}
    animate={{opacity:1,y:0}}
    transition={{duration:1, type:'spring'}}>
        <div className={`${styles.sizedBox} ${styles.flip1}`}>
        </div>
        <h1 className={styles.title}>
          Neetcodes <br></br> Leetcode <br></br>  Challenge
        </h1>
    </motion.div>
  )
}

export default SectionOneLeft