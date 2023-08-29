'use client'
import React, { useState, useEffect,useRef } from "react";
import cn from "classnames";
import styles from '@/styles/DataStructure.module.css';
import { motion } from "framer-motion"

const cards = ["Longest Substring Without Repeating Characters", 
"New Valid Parentheses", 
"Contains Duplicate", "Valid Palindrome"];

const tabVariant = {
  active: {
      backgroundColor: "#53C2AB",
      color:"#4B3E52",
      transition: {
      type: "tween",
      duration: 0.2
      }
  },
  inactive: {
    backgroundColor: "#B7B1F2",
      transition: {
      type: "tween",
      duration: 0.2
      }
  },
  hover:{
    backgroundColor: "#D6F4F3",
    textShadow:"0px 0px 0px rgb(0,0,0,0,0)",
    boxShadow:"0px 0px 0px rgb(0,0,0,0,0)",
    transition:{type: "tween",
    duration: 0.2}
  }
};

  
const tabContentVariant = {
  active: {
    display: "block",
    transition: {
      staggerChildren: 0.2
    }
  },
  inactive: {
    display: "none"
  }
};

const cardVariant = {
  active: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5
    }
  },
  inactive: {
    opacity: 0,
    y: 10,
    transition: {
      duration: 0.5
    }
  }
};


const DataStructureTabs = ({tabs, defaultIndex = 0 }) => {
  const ref = useRef(null);
  const [activeTabIndex, setActiveTabIndex] = useState(0);
  const onTabClick = (index) => {
    console.log("working")
    setActiveTabIndex(index);
  };
  return (
      <div className={styles.tabs}>
        <div ref={ref}>

        <motion.div className={styles.titleList}>
        <TitleBox list={tabs} activeTabIndex={activeTabIndex} onTabClick={onTabClick}></TitleBox>
        </motion.div>
        </div>
        <div className={styles.contentBox}>
        {tabs.map((tab, index) => (
            <TabContent
              key={index}
              id={`${tab.id}-content`}
              active={activeTabIndex === index}
            />
          ))}
        </div>
      </div>
  )
}


const TitleBox = ({list,activeTabIndex, onTabClick}) => {
  const listItems = list.map((myList,index)=>{   
      return (
      <motion.div 
      className={cn("tab",styles.titleBox, { active: activeTabIndex === index })}
      key={index}
      variants={tabVariant}
      whileHover="hover"
      animate={activeTabIndex === index ? "active" : "inactive"}
      >
        <h4 onClick={() => onTabClick(index)}>
            {myList}
            {/* <motion.span variants={tabTextVariant}>{tab.title}</motion.span> */}
        </h4>
      </motion.div>);   
  });   
  return listItems;
}

const TabContent = ({ id, active }) => (
  <motion.div
    role="tabPanel"
    id={id}
    className="tab-content"
    variants={tabContentVariant}
    animate={active ? "active" : "inactive"}
    initial="inactive"
  >
    <div className="cards">
      {cards.map((item, index) => (
        <motion.div key={index} variants={cardVariant} className="content-card">
          <div className={styles.quesBox}>
            <h3>{`${item}`} - Easy</h3>
          </div>
        </motion.div>
      ))}
    </div>
  </motion.div>
);


export default DataStructureTabs;