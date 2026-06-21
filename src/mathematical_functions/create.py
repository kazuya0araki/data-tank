from . import const
import numpy as np

# Parameter
t1 = np.arange(-10.0, 10.1, 0.1)
t2 = np.arange(0.0, 10.1, 0.1)
r1 = np.linspace(-2 * np.pi, 2 * np.pi, 721)
r2 = np.linspace(-1 * np.pi, 1 * np.pi, 361)
r3 = np.linspace(0, 2 * np.pi, 361)
r4 = np.linspace(0, 4 * np.pi, 721)

# Elementary function
def create_linear_function_csv():
    ## linear function
    x = t1
    y = t1
    return np.savetxt("{0}Linear_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=x", color="blue")

def create_quadratic_function_csv():
    ## quadratic function
    x = t1
    y = t1 ** 2
    return np.savetxt("{0}Quadratic_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=x^2", color="orange")

def create_cubic_function_csv():
    ## cubic function
    x = t1
    y = t1 ** 3
    np.savetxt("{0}Cubic_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=x^3", color="red")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_square_root_function_csv():
    ## square root function
    x = t2
    y = t2 ** (1/2)
    np.savetxt("{0}Square_Root_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=x^(1/2)", color="cyan")

def create_cubic_root_function_csv():
    ## cubic root function
    x = t2
    y = t2 ** (1/3)
    np.savetxt("{0}Cubic_Root_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=x^(1/3)", color="green")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_two_to_the_xth_power_function_csv():
    ## 2 ^ x
    x = t1
    y = 2 ** t1
    np.savetxt("{0}Two_to_the_xth_Power_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=2^x", color="yellow")

def create_exponential_x_function_csv():
    ## e ^ x
    x = t1
    y = np.exp(t1)
    np.savetxt("{0}Exponential_X_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(t1, y, label="y=e^x", color="magenta")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_logarithm_function_csv():
    ## logarithm function (natural log)
    x = np.arange(0.1, 10.1, 0.1)
    y = np.log(x)
    np.savetxt("{0}Logarithm_Function.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")

# trigonometric function
def create_sine_function_csv():
    ## sin x
    x = r1
    y = np.sin(r1)
    np.savetxt("{0}Sine.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=sin(x)", color="blue")

def create_cosine_function_csv():
    ## cos x
    x = r1
    y = np.cos(r1)
    np.savetxt("{0}Cosine.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=cos(x)", color="orange")
    # plt.xticks(np.linspace(-2 * np.pi, 2 * np.pi, 9), ["-2π", "-3π/2", "-π", "-π/2", "0", "π/2", "π", "2π/2", "2π"])
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_tangent_function_csv():
    ## tan x
    x = r2
    y = np.tan(r2)
    np.savetxt("{0}Tangent.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="y=tan(x)", color="green", marker=".", ls="None")
    # plt.xticks(np.linspace(-1 * np.pi, np.pi, 5), ["-π", "-π/2", "0", "π/2", "π"])
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

### cosecant csc
# TODO: wip

### secant sec
# TODO: wip

### cotangent cot
# TODO: wip


## hyperbolic function
### sinh
# TODO: wip

### cosh
# TODO: wip

### tanh
# TODO: wip

### sech
# TODO: wip

### csch
# TODO: wip

### coth
# TODO: wip

## inverse hyperbolic functions
### arsinh
# TODO: wip

### arcosh
# TODO: wip

### artanh
# TODO: wip

### arsech
# TODO: wip

### arcsch
# TODO: wip

### arcot
# TODO: wip

# Parametric Representation
def create_cycloid_csv():
    ## cycloid
    x = r3 - np.sin(r3)
    y = 1 - np.cos(r3)
    np.savetxt("{0}Cycloid.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.title("cycloid")
    # plt.plot(x, y, label="a=1", color="blue", marker=".")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_astroid_csv():
    ## astroid
    x = np.cos(r3) ** 3
    y = np.sin(r3) ** 3
    np.savetxt("{0}Astroid.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.title("astroid")
    # plt.plot(x, y, label="a=1", color="blue", marker=".")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_cardioid_csv():
    ## cardioid
    x = (1 + np.cos(r3)) * np.cos(r3)
    y = (1 + np.cos(r3)) * np.sin(r3)
    np.savetxt("{0}Cardioid.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.title("cardioid")
    # plt.plot(x, y, label="a-1", color="blue", marker=".")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

# logarithmic spiral
def create_circle_csv():
    ## circle
    x = np.cos(r3)
    y = np.sin(r3)
    np.savetxt("{0}Circle.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="a=1, b=0", color="blue", marker=".")

def create_general_csv():
    ## general
    x = np.exp(r4 / 4) * np.cos(r4)
    y = np.exp(r4 / 4) * np.sin(r4)
    np.savetxt("{0}Logarithmic_Spiral.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.title("logarithmic spiral")
    # plt.plot(x, y, label="a=1, b=1/4", color="orange", marker=".")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_lissajous_curve_csv():
    ## Lissajous curve
    ### a=1, b=2, ∂=0
    x = np.sin(1 * r4)
    y = np.sin(2 * r4)
    np.savetxt("{0}Lissajous_Curve_1.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="a=1, b=2, ∂=0", color="blue", marker=".")

    ### a=3, b=4, ∂=0
    x = np.sin(3 * r4)
    y = np.sin(4 * r4)
    np.savetxt("{0}Lissajous_Curve_2.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="a=3, b=4, ∂=0", color="orange", marker=".")

    ### a=5, b=6, ∂=0
    x = np.sin(5 * r4)
    y = np.sin(6 * r4)
    np.savetxt("{0}Lissajous_Curve_3.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="a=5, b=6, ∂=0", color="red", marker=".")
    # plt.title("Lissajous curve")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()

def create_involute_curve_csv():
    ## involute curve
    x = np.cos(r4) + r4 * np.sin(r4)
    y = np.sin(r4) - r4 * np.cos(r4)
    np.savetxt("{0}Involute_Curve.csv".format(const.DATA_PATH), np.stack([x, y], 1), fmt="%.10f", delimiter=",", header="x,y", comments="")
    # plt.plot(x, y, label="a=1", color="blue", marker=".")
    # plt.title("involute curve")
    # plt.axhline(0, linewidth=2, color="black")
    # plt.axvline(0, linewidth=2, color="black")
    # plt.legend()
    # plt.show()
