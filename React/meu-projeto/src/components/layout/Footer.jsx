import { FaFacebook, FaInstagram, FaInstagramSquare, FaLinkedin, FaLinkedinIn } from 'react-icons/fa'
import styles from '../css/Footer.module.css'

const Footer = () => 

    <footer>
        <ul className={styles.socialList}>
            <li><FaFacebook/></li>
            <li><FaInstagram/></li>
            <li><FaLinkedin/></li>
            <li><FaLinkedinIn/></li>
        </ul>
    </footer>

export default Footer