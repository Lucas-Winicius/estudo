const NavComponent = ({ link, icon, label }) =>

<a href={link}>
    <i className={`fa fa-${icon}`}></i> {label}
</a>

export default NavComponent