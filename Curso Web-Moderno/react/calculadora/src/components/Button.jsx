import '../styles/Button.css'

const Button = ({ label, operation, double, triple, click }) => 
    <button onClick={e => click && click(label)} className={`
        button
        ${operation ? 'operation' : ''}
        ${double ? 'double' : ''}
        ${triple ? 'triple' : ''}
    `}>
        {label}
    </button>

export default Button