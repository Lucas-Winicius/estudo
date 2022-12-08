import PropTypes from "prop-types"

const Item = ({ content, content2 }) => 

    <>
        <li>{ content } - { content2 }</li>
    </>

Item.propTypes = {
    content: PropTypes.string.isRequired,
    content2: PropTypes.number
}

Item.defaultProps = {
    content: 'Nada foi definido',
    content2: 0,
}

export default Item