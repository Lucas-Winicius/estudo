export default ({ setNome }) => (
    <div>
        <p>Digite seu nome: </p>
        <input type="text" name="" id="" placeholder="Qual seu nome?" onChange={e => setNome(e.target.value)} />
    </div>
)