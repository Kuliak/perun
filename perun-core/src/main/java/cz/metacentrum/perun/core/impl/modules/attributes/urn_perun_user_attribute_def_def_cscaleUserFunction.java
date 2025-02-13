package cz.metacentrum.perun.core.impl.modules.attributes;

import cz.metacentrum.perun.core.api.Attribute;
import cz.metacentrum.perun.core.api.User;
import cz.metacentrum.perun.core.api.exceptions.WrongAttributeValueException;
import cz.metacentrum.perun.core.impl.PerunSessionImpl;
import cz.metacentrum.perun.core.implApi.modules.attributes.UserAttributesModuleAbstract;
import cz.metacentrum.perun.core.implApi.modules.attributes.UserAttributesModuleImplApi;

import java.util.Arrays;
import java.util.List;

/**
 * Check constraint on C-SCALE user function
 *
 * @author Pavel Zlámal <zlamal@cesnet.cz>
 */
public class urn_perun_user_attribute_def_def_cscaleUserFunction extends UserAttributesModuleAbstract implements UserAttributesModuleImplApi {

	private final static List<String> allowedValues = Arrays.asList("expert", "manager", "researcher", "technician", "other");

	/**
	 * Checks if users function has allowed value
	 *
	 * @param sess PerunSession
	 * @param user user
	 * @param attribute Attribute of the user
	 * @throws WrongAttributeValueException if the attribute value has wrong/illegal syntax
	 */
	@Override
	public void checkAttributeSyntax(PerunSessionImpl sess, User user, Attribute attribute) throws WrongAttributeValueException {
		if (attribute.getValue() == null) return;

		if (!allowedValues.contains(attribute.valueAsString())) {
			throw new WrongAttributeValueException(attribute, "Attribute must have one of allowed values: expert, manager, researcher, technician, other.");
		}
	}

}
