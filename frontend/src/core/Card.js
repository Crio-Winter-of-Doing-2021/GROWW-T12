import React, { useState, useContext } from "react";
import ImageHelper from "./helper/ImageHelper";
import { Redirect } from "react-router-dom";
import { addItemToCart, removeItemFromCart } from "./helper/cartHelper";
import { isAuthenticated } from "../auth/helper";
import BotPayloadContext from '../BotPayloadContext';
const Card = ({
    product,
    addtoCart = true,
    removeFromCart = false,
    reload = undefined,
    setReload = (f) => f,
    // function(f){return f}
}) => {
    const [redirect, setRedirect] = useState(false);

    const cartTitle = product ? product.name : "A photo from pexels";
    const cartDescription = product ? product.description : "Default description";
    const cartPrice = product ? product.price : "Default";
    const { value, setValue } = useContext(BotPayloadContext);

    const addToCart = () => {
        setValue("/query_my_cart")
        if (isAuthenticated()) {
            addItemToCart(product, () => setRedirect(true));
            console.log("Added to cart");
        } else {
            console.log("Login Please!");
        }
    };

    const getAredirect = (redirect) => {
        if (redirect) {
            return <Redirect to="/cart" />;
        }
    };

    const showAddToCart = (addToCart) => {
        return (
            addtoCart && (
                <button
                    onClick={addToCart}
                    className="btn btn-block btn-primary text-white mt-2 mb-2"
                >
                    Add to Cart
                </button>
            )
        );
    };

    const showRemoveFromCart = (removeFromCart) => {
        return (
            removeFromCart && (
                <button
                    onClick={() => {
                        //TODO: handle this too
                        removeItemFromCart(product.id);
                        setReload(!reload);

                        console.log("Product removed from cart");
                    }}
                    className="btn btn-block btn-outline-danger mt-2 mb-2"
                >
                    Remove from cart
                </button>
            )
        );
    };

    return (
        <div className="card text-white bg-dark border  ">
            <div className="card-header lead">{cartTitle}</div>
            <div className="card-body">
                {getAredirect(redirect)}
                <ImageHelper product={product} />
                <p className="lead btn-info font-weight-normal text-wrap">
                    {cartDescription}
                </p>
                <p className="btn btn-info rounded  btn-sm px-4">$ {cartPrice}</p>
                <div className="row">
                    <div className="col-12">
                        {showAddToCart(addToCart)}
                    </div>
                    <div className="col-12">
                        {showRemoveFromCart(removeFromCart)}
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Card;
