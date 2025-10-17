declare module "react-twemoji" {
  import { ComponentType, ReactNode } from "react";

  type TwemojiTag = keyof JSX.IntrinsicElements;

  interface TwemojiOptions {
    base?: string;
    folder?: string;
    ext?: string;
    size?: string | number;
    className?: string;
    attributes?: (icon: string, variant?: string) => Record<string, string>;
  }

  interface TwemojiProps {
    tag?: TwemojiTag;
    options?: TwemojiOptions;
    className?: string;
    children?: ReactNode;
  }

  const Twemoji: ComponentType<TwemojiProps>;

  export default Twemoji;
}
