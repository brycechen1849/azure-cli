# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "network virtual-appliance site create",
    is_preview=True,
)
class Create(AAZCommand):
    """Create an Azure network virtual appliance site.

    :example: Create an Azure network virtual appliance site.
        az network virtual-appliance site create -n MyName -g MyRG --appliance-name MyAppliance --address-prefix 10.0.0.0/24 --allow --default --optimize
    """

    _aaz_info = {
        "version": "2021-08-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.network/networkvirtualappliances/{}/virtualappliancesites/{}", "2021-08-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.appliance_name = AAZStrArg(
            options=["--appliance-name"],
            help="The name of Network Virtual Appliance.",
            required=True,
            id_part="name",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="The name of Network Virtual Appliance Site.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.address_prefix = AAZStrArg(
            options=["--address-prefix"],
            help="Address Prefix of Network Virtual Appliance Site.",
        )

        # define Arg Group "Breakout of O365"

        _args_schema = cls._args_schema
        _args_schema.allow = AAZBoolArg(
            options=["--allow"],
            arg_group="Breakout of O365",
            help="Flag to control breakout of o365 allow category. Allowed values: false, true.",
        )
        _args_schema.default = AAZBoolArg(
            options=["--default"],
            arg_group="Breakout of O365",
            help="Flag to control breakout of o365 default category. Allowed values: false, true.",
        )
        _args_schema.optimize = AAZBoolArg(
            options=["--optimize"],
            arg_group="Breakout of O365",
            help="Flag to control breakout of o365 optimize category. Allowed values: false, true.",
        )

        # define Arg Group "Parameters"
        return cls._args_schema

    def _execute_operations(self):
        yield self.VirtualApplianceSitesCreateOrUpdate(ctx=self.ctx)()

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class VirtualApplianceSitesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/networkVirtualAppliances/{networkVirtualApplianceName}/virtualApplianceSites/{siteName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "networkVirtualApplianceName", self.ctx.args.appliance_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "siteName", self.ctx.args.name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2021-08-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("name", AAZStrType, ".name")
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("addressPrefix", AAZStrType, ".address_prefix")
                properties.set_prop("o365Policy", AAZObjectType)

            o365_policy = _builder.get(".properties.o365Policy")
            if o365_policy is not None:
                o365_policy.set_prop("breakOutCategories", AAZObjectType)

            break_out_categories = _builder.get(".properties.o365Policy.breakOutCategories")
            if break_out_categories is not None:
                break_out_categories.set_prop("allow", AAZBoolType, ".allow")
                break_out_categories.set_prop("default", AAZBoolType, ".default")
                break_out_categories.set_prop("optimize", AAZBoolType, ".optimize")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.etag = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.id = AAZStrType()
            _schema_on_200_201.name = AAZStrType()
            _schema_on_200_201.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.address_prefix = AAZStrType(
                serialized_name="addressPrefix",
            )
            properties.o365_policy = AAZObjectType(
                serialized_name="o365Policy",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )

            o365_policy = cls._schema_on_200_201.properties.o365_policy
            o365_policy.break_out_categories = AAZObjectType(
                serialized_name="breakOutCategories",
            )

            break_out_categories = cls._schema_on_200_201.properties.o365_policy.break_out_categories
            break_out_categories.allow = AAZBoolType()
            break_out_categories.default = AAZBoolType()
            break_out_categories.optimize = AAZBoolType()

            return cls._schema_on_200_201


__all__ = ["Create"]
