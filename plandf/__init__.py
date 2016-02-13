from plan_maker import PlanMaker

def read(plan_tuples, conversion_rates=False):

    if conversion_rates:
        try:
            from rates import Rates
            r = Rates()
            p = PlanMaker(plan_tuples, conversion_rates=r.df)
        except:
            """ Could not retrieve currency conversion rates. """
            p = False

    else:
		p = PlanMaker(plan_tuples)

    if p:
        return p.get_value_over_time()
    else:
		return "Could not read the plan_tuples."
