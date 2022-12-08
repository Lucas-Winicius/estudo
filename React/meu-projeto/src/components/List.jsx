import Item from "./Item"

const List = props => {
    return (
        <>
            <h1>Minha Lista</h1>
            <ul>
                <Item content="Ferrari" content2={1985} />
                <Item content="Fiat" content2={1964} />
                <Item content="Ford" content2={1977} />
                <Item content="Renault" content2={2022} />
                <Item/>
            </ul>
        </>
    )
}

export default List