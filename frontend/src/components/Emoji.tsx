import Twemoji from "react-twemoji";

interface EmojiProps {
  symbol: string;
  label?: string;
  className?: string;
}

const options = {
  folder: "svg",
  ext: ".svg",
  className: "emoji__img"
};

function Emoji({ symbol, label, className }: EmojiProps): JSX.Element {
  return (
    <Twemoji
      tag="span"
      options={options}
      className={["emoji", className].filter(Boolean).join(" ")}
    >
      <span role="img" aria-label={label ?? symbol}>
        {symbol}
      </span>
    </Twemoji>
  );
}

export default Emoji;
