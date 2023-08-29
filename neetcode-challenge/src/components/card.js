'use client'
import React from 'react'
import '@coreui/coreui/dist/css/coreui.min.css'
import styles from '@/styles/card.module.css'
import { motion } from "framer-motion"

const Card = () => {
  return (
    <motion.div style={{padding:10}}
    whileHover={{ scale: 1.1 }}
    whileTap={{ scale: 0.9 }}> 
        <div className={styles.card} style={{ width: '18rem'  }}>
          <div className='cardBody'>
            <h2  className={styles.title}> Same Tree </h2>
            <h4  className={styles.subtitle}>Trees</h4>
            <p>IGiven the roots of two binary trees p and q, write a function to check if they are the same or not.</p>
          </div>
          <div>

          </div >
          <div className={styles.cardLinks}>
          <a className={styles.link} target="_blank" rel="noopener noreferrer" href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">Problem</a>
          <a className={styles.link} target="_blank" rel="noopener noreferrer" href="https://leetcode.com/problems/longest-substring-without-repeating-characters/">Code</a>
          </div>
        </div>
    </motion.div>
  )
}

export default Card