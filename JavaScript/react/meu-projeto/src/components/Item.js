import PropTypes from 'prop-types'

function Item({cont, preco}) {
    return (
        <>
            <li>{cont} - R${preco}</li>
        </>
    )
}

Item.propType = {
    cont: PropTypes.string.isRequired,
    preco: PropTypes.number
}

Item.defaultProps = {
    cont: 'undefined',
    preco: 0
}

export default Item