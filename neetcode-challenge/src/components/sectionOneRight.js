import React from 'react'
import styles from '@/styles/Home.module.css'
import Image from 'next/image'
import { motion } from "framer-motion"

const SectionOneRight = () => {
  return (
    <div className={styles.branch2} >
      <div className={styles.sizedBox}>
    </div>
    <motion.div className={styles.container}
    initial={{opacity:0,y:-50}}
    animate={{opacity:1,y:0}}
    transition={{delay:0.5, duration:1}}>
        <Image
            priority
            src="/images/programmer.svg"
            fill="responsive"
            alt="Follow us on Twitter"
        />
    </motion.div>
    
</div>
  )
}

export default SectionOneRight