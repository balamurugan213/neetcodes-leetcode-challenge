import React from 'react'
import styles from '@/styles/Home.module.css'
import Link from 'next/link'

const Navbar = () => {
  return (
    <>
        <nav className={styles.navbar}>
            <div className={styles.navLinks}>
                <Link className={styles.navItem} href="/">Home</Link>
                <Link className={styles.navItem} href="/about">About</Link>
                <Link className={styles.navItem} href="/contact">Contact</Link>
            </div>
      </nav>
    </>
  )
}

export default Navbar