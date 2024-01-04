
$SERVIECS = get-service -Name "*VM*"

foreach ($SERVICE in $SERVICES) {
    # Stop the service
    Stop-Service -Name $SERVICE.Name -Force
    # Disable the service
    Set-Service -Name $SERVICE.Name -StartupType Disabled
}
