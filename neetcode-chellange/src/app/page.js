import React from 'react'
import styles from '@/styles/Home.module.css'

const Homepage = () => {
    return (
    <div className={`${styles.mainPage} ${styles.treeRoot}` }>
        <div className={styles.branch1}>
        <h1 className={styles.title}>
        Neetcodes <br></br> Leetcode <br></br>  Challenge
        </h1>
        <div className={styles.subDetails}>
        <h3>Its a challenge of 150 programs to solve on all different data structure topics.<br></br>
These question are frequently asked in the interviews.</h3>
        </div>
       
        </div>
    </div>
    )
}

export default Homepage