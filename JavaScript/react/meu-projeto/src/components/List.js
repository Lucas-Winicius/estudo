import Item from "./Item"

function List() {
    return (
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item cont='Abobora' preco={20}/>
                <Item cont='Sopa De Abobora' preco={40}/>
                <Item cont='Abobora Na Lata' preco={100}/>
                <Item />
            </ul>
        </>
    )
}



export default List